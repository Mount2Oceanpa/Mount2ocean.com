import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== FETCHING & TESTING LIVE VERCEL DEPLOYMENT ===")

try:
    url_index = "https://mount2ocean-com.vercel.app/index.html"
    req = urllib.request.Request(url_index, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')

    print(f"Successfully fetched live index.html ({len(html)} bytes)")
    
    # Check if switchAuthTab is present in inline script
    print("Contains switchAuthTab in index.html:", "switchAuthTab" in html)
    print("Contains signupView in index.html:", "signupView" in html)

    url_js = "https://mount2ocean-com.vercel.app/app.js"
    req_js = urllib.request.Request(url_js, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_js) as resp:
        js = resp.read().decode('utf-8')

    print(f"Successfully fetched live app.js ({len(js)} bytes)")

    # Count switchAuthTab in live app.js
    matches = [m.start() for m in re.finditer(r'switchAuthTab\s*=\s*function', js)]
    print("Occurrences of 'switchAuthTab = function' in LIVE app.js:", len(matches))
    if len(matches) == 1:
        print("✅ LIVE VERIFICATION SUCCESSFUL! Exactly 1 clean switchAuthTab function in live app.js!")
    else:
        print(f"⚠️ Warning: Found {len(matches)} occurrences")

except Exception as e:
    print(f"Fetch error: {e}")
