import os, glob, re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html'))
print(f"=== FULL WEBSITE DEEP AUDIT & ENHANCEMENT FOR {len(html_files)} PAGES ===")

modified_count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # 1. Update logo links to point to customer_portal.html (homepage)
    content = re.sub(r'<a href="index\.html">\s*<img src="assets/official_logo\.png"', '<a href="customer_portal.html"><img src="assets/official_logo.png"', content)

    # 2. Standardize Header Navigation links if present
    content = content.replace('href="index.html#signin"', 'href="index.html"')
    content = content.replace('href="index.html#signup"', 'href="signup.html"')

    # 3. Ensure all links with href="#" are clean and don't cause page jumps if unhandled
    content = re.sub(r'href="#"\s+onclick="switchAuthTab\(\'signup\'\)"', 'href="signup.html"', content)

    # 4. Enforce high-contrast CSS overrides block in <head> if not already present
    contrast_block = """<style id="m2o-global-alignment-contrast-fix">
/* GLOBAL SECTION ALIGNMENT & CONTRAST GUARANTEE */
body { font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif !important; }
.app-header { max-width: 1320px !important; margin: 0 auto !important; }
.main-container, .portal-wrapper, .page-container { max-width: 1320px !important; margin: 0 auto !important; }
.cust-footer { width: 100% !important; margin-top: 4rem !important; background: #060911 !important; color: #ffffff !important; }
.cust-footer * { color: #ffffff !important; }
.cust-footer a { color: #ffffff !important; text-decoration: none !important; }
.cust-footer a:hover { color: #00f2fe !important; }
.cust-footer-grid { max-width: 1320px !important; margin: 0 auto !important; }
button, input, select, textarea { font-family: inherit !important; }
</style>"""

    if '<style id="m2o-global-alignment-contrast-fix">' not in content:
        content = content.replace('</head>', contrast_block + '\n</head>', 1)

    if content != original:
        modified_count += 1
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Audit and enhancement complete! Updated {modified_count} pages.")
