import urllib.request, re

req = urllib.request.Request('http://locketgold.petervincent.id.vn', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
print('Title:', re.findall(r'<title>(.*?)</title>', html))
for h in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html):
    print('H:', re.sub(r'<[^>]+>', '', h).strip())
for a in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html):
    print('Link:', a[0], '->', re.sub(r'<[^>]+>', '', a[1]).strip())
for p in re.findall(r'<p[^>]*class="[^"]*lead[^"]*"[^>]*>(.*?)</p>', html):
    print('Lead:', re.sub(r'<[^>]+>', '', p).strip())
# Search all occurrences of photobooth
for line in html.splitlines():
    if 'photobooth' in line.lower() or 'photo booth' in line.lower() or 'cấu hình' in line.lower():
        print('LINE:', re.sub(r'<[^>]+>', ' ', line).strip()[:150])
