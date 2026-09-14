"""Stage only public files, preserving project-site routes for local preview."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--base-path', default='/picberry-site/')
args = parser.parse_args()
if not re.fullmatch(r'/(?:[a-z0-9][a-z0-9-]*/)?', args.base_path):
    parser.error('base path must be / or one lowercase directory, for example /picberry-site/')
subprocess.run([sys.executable, str(ROOT / 'scripts/check.py')], check=True)
output = ROOT / '_site'
if output.is_symlink():
    raise SystemExit('Refusing to replace a symlink at _site')
if output.exists():
    shutil.rmtree(output)
destination = output / args.base_path.strip('/')
shutil.copytree(ROOT / 'site', destination)
not_found = destination / '404.html'
not_found.write_text(not_found.read_text().replace('/picberry-site/', args.base_path))
(destination / '.nojekyll').write_text('')
print(f'Built public files: {destination.relative_to(ROOT)}')
