#!/usr/bin/env python3
"""Simple CI check: ensure all markdown links resolve.

* External http(s): HEAD request must return <400.
* Local markdown/file links: target file must exist.
"""
import re, sys, pathlib, urllib.request, urllib.error

MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def check_file(md_path: pathlib.Path):
    errors = []
    content = md_path.read_text(encoding='utf-8')
    for _, link in MD_LINK_RE.findall(content):
        if link.startswith('http'):
            try:
                with urllib.request.urlopen(link) as resp:
                    if resp.status >= 400:
                        errors.append(f'external link {link} returned {resp.status}')
            except Exception as e:
                errors.append(f'external link {link} error: {e}')
        else:
            target = (md_path.parent / link).resolve()
            if not target.exists():
                errors.append(f'local link {link} not found (ref in {md_path})')
    return errors

def main():
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    md_files = list(repo_root.rglob('*.md'))
    all_errs = []
    for f in md_files:
        all_errs.extend(check_file(f))
    if all_errs:
        print('\n'.join(all_errs))
        sys.exit(1)

if __name__ == '__main__':
    main()
