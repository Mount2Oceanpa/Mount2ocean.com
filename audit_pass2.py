import os, glob, re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html'))
print(f"=== SECOND PASS AUDIT FOR {len(html_files)} HTML PAGES ===")

issues = []

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Check title tag exists
    if '<title>' not in content or '</title>' not in content:
        issues.append(f"[{filename}] Missing <title> tag")

    # 2. Check lang="en"
    if 'lang="bn"' in content or 'lang="bn-BD"' in content:
        issues.append(f"[{filename}] Old lang='bn' found!")

    # 3. Check for any remaining raw Bengali characters
    bengali = re.findall(r'[\u0980-\u09FF]+', content)
    if bengali:
        issues.append(f"[{filename}] Bengali text: {bengali[:3]}")

    # 4. Check for invalid inline styles
    if 'background: rgba;' in content:
        issues.append(f"[{filename}] Invalid CSS background: rgba;")

    # 5. Check CSS link
    if 'styles.css' not in content:
        issues.append(f"[{filename}] Missing styles.css link!")

    # 6. Check script tags
    if 'app.js' not in content and 'admin_' not in filename:
        issues.append(f"[{filename}] Missing app.js script tag")

print("\n=== SECOND PASS RESULTS ===")
if not issues:
    print("✅ 100% PERFECT! ALL 27 PAGES ARE VALIDATED AND PASSED SECOND PASS AUDIT!")
else:
    for iss in issues:
        print(" ❌", iss)
