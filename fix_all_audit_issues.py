import os, glob, re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html'))
print(f"=== CLEANING & FIXING ALL AUDIT ISSUES IN {len(html_files)} FILES ===")

# Corrupted Mojibake Replacement Map
mojibake_map = {
    'ðŸ“ ': '&#128205;',  # Location pin
    'ðŸ“': '&#128205;',
    'ðŸ“📍': '&#128205;',
    'ðŸ📍': '&#128205;',
    'ðŸ—ºï¿½': '&#128506;',
    'ðŸ—º': '&#128506;',
    'ðŸ   ': '&#127976;', # Hotel
    'ðŸ✈️': '&#9992;',
    'ðŸ📞': '&#128222;',
    'ðŸ4': '&#128222;',
    'ðŸ': '',             # Leftover junk bytes
}

fixed_files_count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # 1. Fix Mojibake corrupted emoji sequences
    for k, v in mojibake_map.items():
        if k in content:
            content = content.replace(k, v)

    # Clean any remaining standalone ðŸ
    content = content.replace('ðŸ', '')

    # 2. Fix Invalid CSS Syntax "background: rgba;" or "rgba;"
    # Invalid "background: rgba;" -> "background: rgba(15,23,42,0.75);" or "background: #f8fafc;"
    content = re.sub(r'background:\s*rgba\s*;', 'background: rgba(15, 23, 42, 0.75);', content)
    content = re.sub(r'background:\s*rgba\s*([;\s"])', r'background: rgba(15, 23, 42, 0.75)\1', content)
    content = re.sub(r'box-shadow:\s*0\s+4px\s+15px\s+rgba\s*;', 'box-shadow: 0 4px 15px rgba(0,0,0,0.15);', content)
    content = re.sub(r'box-shadow:\s*0\s+0\s+25px\s+rgba\s*;', 'box-shadow: 0 0 25px rgba(0,242,254,0.25);', content)
    content = re.sub(r'box-shadow:\s*0\s+0\s+10px\s+rgba\s*;', 'box-shadow: 0 0 10px rgba(0,242,254,0.3);', content)
    content = re.sub(r'border:\s*1px\s+solid\s+rgba\s*;', 'border: 1px solid rgba(0, 242, 254, 0.3);', content)
    content = re.sub(r'border:\s*2px\s+solid\s+rgba\s*;', 'border: 2px solid rgba(0, 242, 254, 0.3);', content)
    content = re.sub(r'border-top:\s*1px\s+solid\s+rgba\s*;', 'border-top: 1px solid rgba(255,255,255,0.15);', content)

    # 3. Bump CSS cache-bust version to v=v52_final_launch_ready
    content = re.sub(r'styles\.css\?v=[a-zA-Z0-9_]+', 'styles.css?v=v52_final_launch_ready', content)

    # 4. Fix template string placeholders in img src fallback
    content = content.replace('src="${pkg.image}"', 'src="${pkg.image || \'assets/official_logo.png\'}" onerror="this.src=\'assets/official_logo.png\'"')
    content = content.replace('src="${item.src}"', 'src="${item.src || \'assets/official_logo.png\'}" onerror="this.src=\'assets/official_logo.png\'"')

    if content != original:
        fixed_files_count += 1
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Done! Updated and cleaned {fixed_files_count} HTML files.")
