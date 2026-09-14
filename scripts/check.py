"""Validate authored HTML, routes, assets, and the site's static-only contract."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
PREFIX = '/picberry-site/'
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.main = 0
        self.title = False
        self.lang = False
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag in ('script', 'iframe', 'form', 'base'):
            errors.append(f'{self.path}: unsupported active element <{tag}>')
        if any(key.lower().startswith('on') for key in attr):
            errors.append(f'{self.path}: inline event handler')
        if 'id' in attr:
            if attr['id'] in self.ids:
                errors.append(f'{self.path}: duplicate id {attr["id"]}')
            self.ids.add(attr['id'])
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.title |= tag == 'title'
        self.lang |= tag == 'html' and attr.get('lang') == 'en'
        self.viewport |= tag == 'meta' and attr.get('name') == 'viewport'
        if tag == 'img' and 'alt' not in attr:
            errors.append(f'{self.path}: image missing alt attribute')
        for key in ('src', 'href'):
            if key in attr and tag != 'base':
                self.refs.append((tag, key, attr[key]))


pages = {}
for path in sorted(SITE.rglob('*.html')):
    page = Page(path.relative_to(SITE))
    page.feed(path.read_text())
    pages[path.resolve()] = page
    if page.h1 != 1 or page.main != 1 or not (page.title and page.lang and page.viewport):
        errors.append(f'{page.path}: require one h1/main, title, lang=en, and viewport')

for path, page in pages.items():
    for tag, key, ref in page.refs:
        url = urlsplit(ref)
        if url.scheme in ('https', 'mailto'):
            if key == 'src' or tag == 'link':
                errors.append(f'{page.path}: externally loaded resource {ref}')
            if url.scheme == 'mailto' and url.path != 'milanvandal@gmail.com':
                errors.append(f'{page.path}: unexpected public email')
            continue
        if url.scheme or url.netloc:
            errors.append(f'{page.path}: unsupported URL {ref}')
            continue
        if not url.path:
            target = path
        elif url.path.startswith('/'):
            if not url.path.startswith(PREFIX):
                errors.append(f'{page.path}: link loses GitHub project prefix: {ref}')
                continue
            target = SITE / unquote(url.path.removeprefix(PREFIX))
        else:
            target = path.parent / unquote(url.path)
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.is_relative_to(SITE) or not target.is_file():
            errors.append(f'{page.path}: broken local link {ref}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{page.path}: broken fragment {ref}')
        if tag == 'a' and url.path.endswith(('.html', '.md')):
            errors.append(f'{page.path}: public navigation must use directory URLs: {ref}')

for relative in ('index.html', 'privacy/index.html', 'support/index.html', '404.html', 'assets/site.css', 'assets/app-icon.png'):
    if not (SITE / relative).is_file():
        errors.append(f'missing required route or resource: {relative}')

css = (SITE / 'assets/site.css').read_text()
if '@import' in css or 'url(' in css:
    errors.append('CSS must not load additional resources')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'Validated {len(pages)} HTML pages: routes, local assets, fragments, accessibility basics, and static-only content.')
