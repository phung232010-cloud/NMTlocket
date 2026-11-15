import urllib.request, re

req = urllib.request.Request('http://locketgold.petervincent.id.vn/guide', headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    for h in re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html):
        print('H:', re.sub(r'<[^>]+>', '', h).strip())
    for p in re.findall(r'<p[^>]*>(.*?)</p>', html):
        txt = re.sub(r'<[^>]+>', '', p).strip()
        if len(txt) > 20:
            print('P:', txt[:150])
except Exception as e:
    print('Error:', e)
