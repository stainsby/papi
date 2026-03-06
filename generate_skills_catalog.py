#!/usr/bin/env python3
"""
Generate a markdown catalog of all instructions and skills with their descriptions and contents.
"""

import os
from pathlib import Path
import yaml

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                # Find the closing ---
                end_index = content.find('---', 3)
                if end_index != -1:
                    frontmatter_str = content[3:end_index].strip()
                    try:
                        return yaml.safe_load(frontmatter_str)
                    except yaml.YAMLError:
                        return {}
    except Exception:
        pass
    return {}

def list_directory_files(dir_path):
    """List all files in a directory (excluding SKILL.md)."""
    files = []
    
    try:
        for root, dirs, filenames in os.walk(dir_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in sorted(filenames):
                if file.startswith('.'):
                    continue
                    
                if file == 'SKILL.md':
                    continue
                    
                rel_path = os.path.relpath(os.path.join(root, file), dir_path)
                files.append(rel_path)
    except Exception:
        pass
    
    return files

def generate_catalog():
    """Generate the catalog markdown."""
    base_path = Path(__file__).parent
    instructions_path = base_path / 'instructions'
    skills_path = base_path / 'skills'
    
    output = []
    output.append("# PAPI Skills Catalog\n\n")
    output.append("Complete listing of all instructions and skills with their descriptions and contents.\n\n")
    output.append(f"Generated: {os.popen('date').read().strip()}\n")
    
    # Process Instructions
    output.append("\n## Instructions\n\n")
    
    if instructions_path.exists():
        for instr_file in sorted(instructions_path.glob('*.md')):
            frontmatter = extract_frontmatter(instr_file)
            rel_path = instr_file.relative_to(base_path)
            description = frontmatter.get('description', '')
            
            if description:
                output.append(f"{description}\n\n")
            output.append(f"[{rel_path}]({rel_path})\n")
            
            # List files in instruction directory if it exists
            instr_dir = instr_file.parent / instr_file.stem
            if instr_dir.exists() and instr_dir.is_dir():
                files = list_directory_files(instr_dir)
                if files:
                    output.append("Contents:\n")
                    for f in files:
                        output.append(f"- `{f}`\n")
    
    # Process Skills
    output.append("\n## Skills\n\n")
    
    if skills_path.exists():
        for skill_dir in sorted(skills_path.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
            
            skill_md = skill_dir / 'SKILL.md'
            if skill_md.exists():
                frontmatter = extract_frontmatter(skill_md)
                name = frontmatter.get('name', skill_dir.name)
                description = frontmatter.get('description', 'No description available.')
                
                output.append(f"### {name}\n\n")
                output.append(f"{description}\n\n")
                rel_dir = skill_dir.relative_to(base_path)
                skill_file = str(rel_dir / "SKILL.md").replace('\\', '/')
                output.append(f"[{skill_file}]({skill_file})\n")
                
                # List all files in skill directory
                files = list_directory_files(skill_dir)
                if files:
                    output.append("\nContents:\n")
                    for f in files:
                        file_link = str(rel_dir / f).replace('\\', '/')
                        output.append(f"- [{f}]({file_link})\n")
                output.append("\n")
    
    return ''.join(output).rstrip() + '\n'

if __name__ == '__main__':
    catalog = generate_catalog()
    
    # Write to file
    output_path = Path(__file__).parent / 'SKILLS_CATALOG.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(catalog)
    
    print(f"Catalog generated: {output_path}")
