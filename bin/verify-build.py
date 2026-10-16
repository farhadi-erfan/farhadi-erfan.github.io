"""Reject incomplete production builds before publishing them."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

root = Path('_site').resolve()
for required in ['index.html', '404.html', 'assets/css/main.css', 'assets/js/common.js']:
    path = root / required
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f'Missing or empty built file: {required}')


class Assets(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('src') if tag == 'script' else attrs.get('href') if tag == 'link' and attrs.get('rel') == 'stylesheet' else None
        if not url:
            return
        parsed = urlparse(url)
        if parsed.scheme or parsed.netloc:
            return
        path = (root / unquote(parsed.path).lstrip('/')).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise SystemExit(f'Homepage references a missing local asset: {url}')


html = (root / 'index.html').read_text()
if 'Erfan' not in html:
    raise SystemExit('Homepage does not contain the expected site identity')
Assets().feed(html)
if (root / 'dashboard').exists():
    raise SystemExit('The static site must not own the dashboard path')
print('Built homepage, error page, CSS, JS and local asset references verified.')
