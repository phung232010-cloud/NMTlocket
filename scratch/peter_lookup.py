import urllib.request, re

req = urllib.request.Request('http://locketgold.petervincent.id.vn/lookup', headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    for a in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html):
        print('Link:', a[0], '->', a[1])
    for f in re.findall(r'<form[^>]*action="([^"]*)"[^>]*>', html):
        print('Form action:', f)
    for line in html.splitlines():
        if any(k in line.lower() for k in ['mobileconfig', 'download', 'api', 'profile', 'dns']):
            print('LINE:', re.sub(r'<[^>]+>', ' ', line).strip()[:150])
except Exception as e:
    print('Error:', e)
