import os, glob, re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html'))
print(f"=== FULL WEBSITE AUDIT FOR {len(html_files)} PAGES ===")

issues = []

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # 1. Bengali Character Check
    bengali_matches = re.findall(r'[\u0980-\u09FF]+', content)
    if bengali_matches:
        issues.append(f"[{filename}] Bengali text found: {bengali_matches[:5]}")

    # 2. Mojibake / Corrupted Character Check
    mojibake_patterns = [r'à§³', r'MalÃ©', r'â‚µ', r'Ã©', r'ðŸ', r'ï¿½', r'\?{3,}']
    for pattern in mojibake_patterns:
        if re.search(pattern, content):
            issues.append(f"[{filename}] Corrupted mojibake pattern matched '{pattern}'")

    # 3. Currency symbol check (৳)
    if '৳' in content:
        issues.append(f"[{filename}] Bengali Taka symbol ৳ found! Should be 'BDT '")

    # 4. Cache-bust version check
    if 'styles.css' in content and 'v=v51_zero_invisible_contrast' not in content and 'v=v52_final_launch_ready' not in content:
        issues.append(f"[{filename}] Outdated CSS cache bust version!")

    # 5. Broken image links or missing alt attributes
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\'\s>]+)["\']', content)
    for src in img_srcs:
        if not src.startswith('http') and not src.startswith('data:') and not os.path.exists(src):
            issues.append(f"[{filename}] Missing image asset: {src}")

    # 6. Check unclosed tags or broken inline style syntax like background: rgba;
    if 'background: rgba;' in content or 'background: rgba ' in content:
        issues.append(f"[{filename}] Invalid CSS syntax 'background: rgba;' found")

print("\n=== AUDIT SUMMARY ===")
if not issues:
    print("✅ PERFECT AUDIT! No broken characters, no missing assets, no invalid CSS syntax found!")
else:
    print(f"Found {len(issues)} issues to fix:")
    for iss in issues:
        print(" -", iss)
