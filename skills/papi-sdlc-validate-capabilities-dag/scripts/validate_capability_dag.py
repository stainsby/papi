#!/usr/bin/env python3
"""
Capability Dependency DAG Validator

Extracts capability dependencies from component specification files and validates
that they form a valid Directed Acyclic Graph (DAG).

Checks for:
- Cycles in the dependency graph
- Orphaned components (no incoming or outgoing edges)
- Invalid capability references (referenced capabilities that don't exist)

Usage:
    python validate_capability_dag.py [--specs-dir DIRECTORY] [--output REPORT_FILE]
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml

try:
    import networkx as nx
except ImportError:
    print("ERROR: networkx is required. Install with: pip install networkx", file=sys.stderr)
    sys.exit(1)


def extract_yaml_blocks(markdown_content: str) -> List[str]:
    """
    Extract all YAML code blocks from markdown content.
    Args:
        markdown_content: The markdown file content as a string
        
    Returns:
        List of YAML block contents (without the fence markers)
    """
    # Pattern to match ```yaml ... ``` blocks
    pattern = r'```yaml\s*\n(.*?)\n```'
    matches = re.findall(pattern, markdown_content, re.DOTALL)
    return matches


def parse_dependencies(yaml_content: str) -> Tuple[str, Dict[str, List[Tuple[str, str]]]]:
    """
    Parse the dependencies section from a YAML block.
    
    Format:
    component: CMP.COMPONENT_CODE
    dependencies:
      CAP.CAPABILITY1:
        - CMP.OTHER1:
          - CAP.SOME_CAPABILITY
          - CAP.ANOTHER_CAPABILITY
        - CMP.OTHER2:
          - CAP.YET_ANOTHER_CAPABILITY
    
    Args:
        yaml_content: YAML content as string
        
    Returns:
        Tuple of (component_code, dependencies_dict) where:
        - component_code: The component code from the YAML
        - dependencies_dict: Maps capability codes to list of (component, capability) tuples
    """
    try:
        data = yaml.safe_load(yaml_content)
        if not data or not isinstance(data, dict):
            return "", {}
        
        component_code = data.get('component', '')
        if not component_code:
            print("WARNING: No 'component' field in YAML block", file=sys.stderr)
            return "", {}
        
        if 'dependencies' not in data:
            return component_code, {}
        
        deps = data['dependencies']
        if not isinstance(deps, dict):
            print(f"WARNING: 'dependencies' is not a dict in {component_code}, "
                  f"got {type(deps).__name__}", file=sys.stderr)
            return component_code, {}
        
        result: Dict[str, List[Tuple[str, str]]] = {}
        
        for cap, dep_list in deps.items():
            if dep_list is None or dep_list == []:
                result[cap] = []
            elif isinstance(dep_list, list):
                parsed_deps = []
                for item in dep_list:
                    if isinstance(item, dict):
                        # Nested format: {CMP.X: [CAP.Y, CAP.Z]}
                        for component, capabilities in item.items():
                            if capabilities and isinstance(capabilities, list):
                                for capability in capabilities:
                                    parsed_deps.append((component, capability))
                    elif isinstance(item, str):
                        # Old flat format: shouldn't happen in valid specs
                        print(f"WARNING: Flat dependency format: {item}",
                              file=sys.stderr)
                result[cap] = parsed_deps
            else:
                result[cap] = []
        return component_code, result
    except yaml.YAMLError as e:
        print(f"WARNING: Failed to parse YAML: {e}", file=sys.stderr)
        return "", {}


def extract_component_code(markdown_content: str) -> str:
    """
    Extract the component code from the markdown frontmatter or content.
    Args:
        markdown_content: The markdown file content
        
    Returns:
        Component code string or empty string if not found
    """
    # Try to find in frontmatter
    frontmatter_match = re.search(r'^code:\s*(\S+)', markdown_content, re.MULTILINE)
    if frontmatter_match:
        return frontmatter_match.group(1)
    # Try to find in body: **Code:** `CMP.X.Y`
    code_match = re.search(r'\*\*Code:\*\*\s*`([^`]+)`', markdown_content)
    if code_match:
        return code_match.group(1)
    return ""


def find_spec_files(specs_dir: Path) -> List[Path]:
    """
    Find all component specification markdown files.
    Args:
        specs_dir: Directory to search for specs
        
    Returns:
        List of Path objects for spec files
    """
    # Look for markdown files, excluding templates and certain directories
    spec_files = []
    for md_file in specs_dir.rglob('*.md'):
        # Skip templates, tasks, and other non-spec directories
        path_parts = md_file.parts
        if any(skip in path_parts for skip in ['templates', 'tasks', 'IDEAS.md', 'README.md']):
            continue
        spec_files.append(md_file)
    return spec_files


def build_dependency_graph(specs_dir: Path) -> Tuple[nx.DiGraph, Dict[str, Path], Set[str]]:
    """
    Build a directed graph with two node types:
    - Component nodes (e.g., CMP.A, CMP.B)
    - Capability nodes (e.g., CMP.A.CAP.STORAGE, CMP.B.CAP.VALIDATION)
    
    Capability names are qualified with their providing component's code to form
    globally unique identifiers, as specified by the component model:
    "If this component is CMP.B and you define CAP.STORAGE below, it is
    implicitly CMP.B.CAP.STORAGE in the global dependency graph."
    
    Edges:
    - Component -> Capability: component provides this capability
    - Capability -> Capability: capability depends on another capability
    
    Args:
        specs_dir: Directory containing component specifications
        
    Returns:
        Tuple of (graph, file_map, all_capabilities)
        - graph: NetworkX directed graph with node_type attribute
        - file_map: Mapping of qualified capability codes to their source files
        - all_capabilities: Set of all qualified capability codes defined
    """
    spec_files = find_spec_files(specs_dir)
    print(f"Found {len(spec_files)} specification files")
    
    # --- First pass: collect all component codes and parsed data ---
    parsed_specs: List[Tuple[Path, str, Dict[str, List[Tuple[str, str]]]]] = []
    all_component_codes: Set[str] = set()
    
    for spec_file in spec_files:
        try:
            content = spec_file.read_text(encoding='utf-8')
            yaml_blocks = extract_yaml_blocks(content)
            
            for yaml_block in yaml_blocks:
                component_code, deps = parse_dependencies(yaml_block)
                if component_code:
                    all_component_codes.add(component_code)
                    parsed_specs.append((spec_file, component_code, deps))
        except Exception as e:
            print(f"ERROR processing {spec_file}: {e}", file=sys.stderr)
            continue
    
    # --- Build component code resolution map (suffix -> full code) ---
    # Allows specs to reference components by suffix (e.g., X.RT.RUST instead
    # of ALL_FORMS.APP.X.RT.RUST) as long as the suffix is unambiguous.
    _code_resolution: Dict[str, str | None] = {}
    for code in all_component_codes:
        parts = code.split('.')
        for i in range(len(parts)):
            suffix = '.'.join(parts[i:])
            if suffix in _code_resolution:
                if _code_resolution[suffix] != code:
                    _code_resolution[suffix] = None  # ambiguous
            else:
                _code_resolution[suffix] = code
    
    def resolve_component_code(ref: str) -> str:
        """Resolve a potentially short component reference to its full code."""
        if ref in all_component_codes:
            return ref  # already a full code
        resolved = _code_resolution.get(ref)
        if resolved:
            return resolved
        print(f"WARNING: Could not resolve component reference '{ref}'",
              file=sys.stderr)
        return ref  # unresolved — use as-is
    
    # --- Second pass: build graph with qualified capability names ---
    G = nx.DiGraph()
    file_map: Dict[str, Path] = {}
    all_capabilities: Set[str] = set()
    
    for spec_file, component_code, deps in parsed_specs:
        # Add component node (add_node merges attrs on existing nodes)
        G.add_node(
            component_code,
            node_type='component',
            source_file=str(spec_file)
        )
        
        for capability, dep_list in deps.items():
            # Qualify capability with its providing component
            qualified_cap = f"{component_code}.{capability}"
            
            all_capabilities.add(qualified_cap)
            file_map[qualified_cap] = spec_file
            
            # add_node merges attrs on existing nodes, so auto-created
            # dependency targets get node_type set when their spec is processed
            G.add_node(
                qualified_cap,
                node_type='capability',
                source_file=str(spec_file)
            )
            
            # Component provides this capability
            G.add_edge(component_code, qualified_cap)
            
            # Add capability dependencies (qualified with dep component)
            for dep_component, dep_capability in dep_list:
                resolved_dep = resolve_component_code(dep_component)
                qualified_dep_cap = f"{resolved_dep}.{dep_capability}"
                G.add_edge(qualified_cap, qualified_dep_cap)
    
    return G, file_map, all_capabilities


def validate_graph(G: nx.DiGraph, all_capabilities: Set[str]) -> dict:
    """
    Validate the dependency graph and collect issues.
    Args:
        G: Directed graph of dependencies
        all_capabilities: Set of all defined capability codes
        
    Returns:
        Dictionary containing validation results and issues
    """
    # Separate internal and external nodes
    internal_components = set()
    external_components = set()
    internal_capabilities = set()
    external_capabilities = set()
    
    for node in G.nodes():
        node_type = G.nodes[node].get('node_type')
        # External components/capabilities contain '.X.' in their qualified path
        # or start with 'X.' (for top-level externals)
        is_external = '.X.' in node or node.startswith('X.')
        
        if node_type == 'component':
            if is_external:
                external_components.add(node)
            else:
                internal_components.add(node)
        elif node_type == 'capability':
            if is_external:
                external_capabilities.add(node)
            else:
                internal_capabilities.add(node)
    
    results = {
        'is_dag': True,
        'cycles': [],
        'orphans': [],
        'invalid_refs': [],
        'total_capabilities': len(all_capabilities),
        'total_edges': G.number_of_edges(),
        'internal_components': len(internal_components),
        'external_components': len(external_components),
        'internal_capabilities': len(internal_capabilities),
        'external_capabilities': len(external_capabilities),
    }
    # Check if it's a DAG
    try:
        results['is_dag'] = nx.is_directed_acyclic_graph(G)
        if not results['is_dag']:
            # Find cycles
            try:
                cycles = list(nx.simple_cycles(G))
                results['cycles'] = cycles
            except Exception as e:
                results['cycles'] = [f"Error finding cycles: {e}"]
    except Exception as e:
        results['is_dag'] = False
        results['cycles'] = [f"Error checking DAG: {e}"]
    # Find orphaned nodes (no connections at all)
    for node in G.nodes():
        in_degree = G.in_degree(node)
        out_degree = G.out_degree(node)
        if in_degree == 0 and out_degree == 0:
            results['orphans'].append(node)
    # Find invalid references (capabilities referenced but not defined)
    for node in G.nodes():
        for successor in G.successors(node):
            if successor not in all_capabilities:
                results['invalid_refs'].append({
                    'from': node,
                    'to': successor,
                    'reason': 'Referenced capability not defined'
                })
    return results


def generate_report(results: dict, output_file: Path = None) -> str:
    """
    Generate a human-readable validation report.
    Args:
        results: Validation results dictionary
        output_file: Optional path to write report to
        
    Returns:
        Report text
    """
    lines = []
    lines.append("=" * 80)
    lines.append("CAPABILITY DEPENDENCY REPORT")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Internal Components: {results['internal_components']}")
    lines.append(f"External Components: {results['external_components']}")
    lines.append(f"Internal Capabilities: {results['internal_capabilities']}")
    lines.append(f"External Capabilities: {results['external_capabilities']}")
    lines.append(f"Total Capabilities: {results['total_capabilities']}")
    lines.append(f"Total Dependencies: {results['total_edges']}")
    lines.append(f"Is Valid DAG: {'✓ YES' if results['is_dag'] else '✗ NO'}")
    lines.append("")
    # Cycles
    if results['cycles']:
        lines.append("CYCLES DETECTED:")
        lines.append("-" * 80)
        for i, cycle in enumerate(results['cycles'], 1):
            if isinstance(cycle, str):
                lines.append(f"  {i}. {cycle}")
            else:
                cycle_str = ' → '.join(cycle + [cycle[0]])
                lines.append(f"  {i}. {cycle_str}")
        lines.append("")
    else:
        lines.append("✓ No cycles detected")
        lines.append("")
    # Orphans
    if results['orphans']:
        lines.append("ORPHANED CAPABILITIES:")
        lines.append("-" * 80)
        lines.append("(Capabilities with no dependencies and not used by any other capability)")
        for orphan in results['orphans']:
            lines.append(f"  - {orphan}")
        lines.append("")
    else:
        lines.append("✓ No orphaned capabilities")
        lines.append("")
    # Invalid references
    if results['invalid_refs']:
        lines.append("INVALID REFERENCES:")
        lines.append("-" * 80)
        lines.append("(Capabilities referenced but not defined in any spec)")
        for ref in results['invalid_refs']:
            lines.append(f"  - {ref['from']} → {ref['to']}")
            lines.append(f"    Reason: {ref['reason']}")
        lines.append("")
    else:
        lines.append("✓ No invalid references")
        lines.append("")
    # Summary
    lines.append("=" * 80)
    total_issues = len(results['cycles']) + len(results['orphans']) + len(results['invalid_refs'])
    if total_issues == 0 and results['is_dag']:
        lines.append("✓ VALIDATION PASSED - No issues found")
    else:
        lines.append(f"✗ VALIDATION FAILED - {total_issues} issue(s) found")
    lines.append("=" * 80)
    report = '\n'.join(lines)
    if output_file:
        output_file.write_text(report, encoding='utf-8')
        print(f"Report written to: {output_file}")
    return report


def main():
    parser = argparse.ArgumentParser(
        description='Validate capability dependency DAG from component specifications'
    )
    parser.add_argument(
        '--specs-dir',
        type=Path,
        default=Path('docs/components'),
        help='Directory containing component specifications (default: docs/components)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output file for validation report (default: print to stdout)'
    )
    args = parser.parse_args()
    if not args.specs_dir.exists():
        print(f"ERROR: Specifications directory not found: {args.specs_dir}", file=sys.stderr)
        sys.exit(1)
    print("Building dependency graph...")
    graph, file_map, all_capabilities = build_dependency_graph(args.specs_dir)
    print("Validating graph...")
    results = validate_graph(graph, all_capabilities)
    print("\nGenerating report...")
    report = generate_report(results, args.output)
    if not args.output:
        print("\n")
        print(report)
    # Exit with error code if validation failed
    total_issues = len(results['cycles']) + len(results['invalid_refs'])
    if not results['is_dag'] or total_issues > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
