import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

white_override = """<style id="force-showcase-all-white">
/* FORCE ALL TEXT IN LEFT SHOWCASE PANEL TO 100% PURE WHITE & BRIGHT CYAN */
body .showcase-panel,
body .showcase-panel *,
body .showcase-panel h1,
body .showcase-panel h2,
body .showcase-panel h3,
body .showcase-panel h4,
body .showcase-panel p,
body .showcase-panel span,
body .showcase-panel li,
body .showcase-panel div,
body .showcase-desc,
body #previewTitle,
body #previewDesc {
  color: #ffffff !important;
}

body .showcase-panel strong,
body .showcase-panel b,
body .feature-list li strong {
  color: #00f2fe !important;
  font-weight: 800 !important;
}

body .showcase-panel .badge-pill,
body .showcase-panel .badge-pill * {
  color: #00f2fe !important;
  background: rgba(0, 242, 254, 0.15) !important;
  border-color: #00f2fe !important;
}
</style>"""

if '<style id="force-showcase-all-white">' in content:
    start = content.find('<style id="force-showcase-all-white">')
    end = content.find('</style>', start) + 8
    content = content[:start] + content[end:]

content = content.replace('</head>', white_override + '\n</head>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% pure white override for showcase panel text!")
