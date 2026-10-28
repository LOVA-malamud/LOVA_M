#!/usr/bin/env python3
"""Read-only content, syntax, notebook and relative Markdown link checks.

Run from anywhere: python3 /path/to/LOVA_M/docs/tools/verify_repository.py
Exit 1 means an organization regression; existing exercise errors are reported
separately and do not get rewritten automatically.
"""
from pathlib import Path
from urllib.parse import unquote
import ast
import hashlib
import json
import os
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
manifest = json.loads((ROOT / 'docs/migration-map.json').read_text())
missing, altered, syntax, notebook_issues, links = [], [], [], [], []
python_count = notebook_count = cells = 0
for entry in manifest:
    path = ROOT / entry['new_path']
    if not path.is_file():
        missing.append(entry['new_path'])
        continue
    if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256_after']:
        # Finder may update metadata without changing any learning material.
        if path.name != '.DS_Store':
            altered.append(entry['new_path'])
    if path.suffix == '.py' or (not path.suffix and path.name != '.DS_Store'
                               and path.read_text(errors='replace').lstrip().startswith(('import ', 'from '))):
        python_count += 1
        try:
            ast.parse(path.read_text(), filename=str(path))
        except SyntaxError as exc:
            syntax.append([entry['new_path'], exc.lineno, exc.msg])
    if path.suffix == '.ipynb':
        notebook_count += 1
        try:
            notebook = json.loads(path.read_text())
            assert notebook['nbformat'] == 4 and isinstance(notebook['cells'], list)
            for number, cell in enumerate(notebook['cells'], 1):
                if cell['cell_type'] == 'code':
                    cells += 1
                    source = ''.join(cell['source'])
                    if source.lstrip().startswith(('%', '!')):
                        continue
                    try:
                        ast.parse(source)
                    except SyntaxError as exc:
                        notebook_issues.append([entry['new_path'], number, exc.msg])
        except (ValueError, KeyError, AssertionError) as exc:
            notebook_issues.append([entry['new_path'], str(exc)])
markdown_files = []
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in {'.git', '.venv', '.venv-tf', '__pycache__'}]
    markdown_files.extend(Path(base) / f for f in files if f.endswith('.md'))
for path in markdown_files:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        target = unquote(target.split('#')[0])
        if target and not (path.parent / target).exists():
            links.append([str(path.relative_to(ROOT)), target])
report = dict(original_files=len(manifest), missing=missing, unexpected_content_changes=altered,
              python_files=python_count, python_syntax_errors=syntax, notebooks=notebook_count,
              notebook_code_cells=cells, notebook_existing_issues=notebook_issues,
              broken_markdown_links=links)
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(missing or altered or syntax or links))
