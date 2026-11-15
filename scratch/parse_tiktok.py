import json, re

path = r'C:/Users/bestn/.gemini/antigravity/brain/45401f56-2e03-4cd4-9c1a-b416c5e0fc55/.system_generated/steps/865/output.txt'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    scope = data.get('__DEFAULT_SCOPE__', {})
    print('Scope keys:', list(scope.keys()))
    video_detail = scope.get('webapp.video-detail', {})
    item = video_detail.get('itemInfo', {}).get('itemStruct', {})
    print('DESC:', item.get('desc'))
    print('AUTHOR:', item.get('author', {}).get('uniqueId'))
    print('VIDEO URL:', item.get('video', {}).get('playAddr'))
    for tag in item.get('textExtra', []):
        print('TAG:', tag.get('hashtagName'))
else:
    print('Not found, searching text lines')
    for line in text.splitlines():
        if any(w in line.lower() for w in ['locket', 'photobooth', 'gold', 'github', 'bin.hay.ho']):
            print('Line:', line[:200])
