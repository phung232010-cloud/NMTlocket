import urllib.request, re, json

url = 'https://www.tiktok.com/@bin.hay.ho5/video/7707070033578528001'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("HTML length:", len(html))
        # Look for SIGI_STATE or __UNIVERSAL_DATA_FOR_REHYDRATION__
        for m in re.finditer(r'<script id="([^"]+)"[^>]*>(.*?)</script>', html, re.DOTALL):
            sid = m.group(1)
            content = m.group(2)
            if 'SIGI_STATE' in sid or '__UNIVERSAL_DATA' in sid:
                print("Found script id:", sid)
                try:
                    data = json.loads(content)
                    print("Keys:", list(data.keys())[:10])
                    # search recursively for string
                    s = json.dumps(data, ensure_ascii=False)
                    for phrase in ['locket', 'photobooth', 'photo booth', 'conf', 'github']:
                        idx = s.lower().find(phrase)
                        if idx != -1:
                            print(f"Match '{phrase}':", s[max(0, idx-50):min(len(s), idx+200)])
                except Exception as e:
                    print("JSON error:", e)
        # Search title and og tags
        for m in re.finditer(r'<meta property="og:([^"]+)" content="([^"]+)"', html):
            print("OG:", m.group(1), "->", m.group(2))
        for m in re.finditer(r'<meta name="description" content="([^"]+)"', html):
            print("Desc:", m.group(1))
except Exception as e:
    import traceback
    traceback.print_exc()
