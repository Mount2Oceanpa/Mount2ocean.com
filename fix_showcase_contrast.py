import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix body tag class
content = content.replace('<body class="dark-theme light-theme">', '<body class="dark-theme">')
content = content.replace('<body class="light-theme dark-theme">', '<body class="dark-theme">')

# 2. Add ultra-explicit showcase panel CSS block
showcase_override = """<style id="showcase-contrast-fix">
/* SHOWCASE PANEL HIGH CONTRAST DARK THEME GUARANTEE */
body .showcase-panel {
  background: linear-gradient(135deg, #0b132b 0%, #1c2541 60%, #0b132b 100%) !important;
  border: 1.5px solid rgba(0, 242, 254, 0.35) !important;
  border-radius: 24px !important;
  padding: 2.5rem !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4) !important;

}
body .showcase-heading {
  color: #ffffff !important;
  font-size: 2.5rem !important;
  font-weight: 900 !important;
  line-height: 1.25 !important;
  margin-bottom: 1.2rem !important;

}
body .showcase-desc, body .showcase-desc * {
  color: #e2e8f0 !important;
  font-size: 1.05rem !important;
  line-height: 1.7 !important;

}
body .showcase-desc strong {
  color: #00f2fe !important;
  font-weight: 800 !important;

}
body .badge-pill {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  background: rgba(0, 242, 254, 0.15) !important;
  border: 1.5px solid #00f2fe !important;
  color: #00f2fe !important;
  padding: 0.4rem 1rem !important;
  border-radius: 20px !important;
  font-weight: 800 !important;
  font-size: 0.85rem !important;
  margin-bottom: 1.5rem !important;

}
body .pulse-dot {
  width: 8px !important;
  height: 8px !important;
  background: #00f2fe !important;
  border-radius: 50% !important;
  box-shadow: 0 0 10px #00f2fe !important;

}
body .role-preview-card {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(0, 242, 254, 0.4) !important;
  border-radius: 16px !important;
  padding: 1.4rem !important;
  margin: 1.8rem 0 !important;

}
body #previewTitle {
  color: #ffffff !important;
  font-size: 1.15rem !important;
  font-weight: 800 !important;
  margin-bottom: 0.4rem !important;

}
body #previewDesc {
  color: #cbd5e1 !important;
  font-size: 0.95rem !important;
  line-height: 1.6 !important;

}
body .feature-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 1.5rem 0 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 1.1rem !important;

}
body .feature-list li {
  display: flex !important;
  align-items: center !important;
  gap: 0.85rem !important;

}
body .feature-list li span, body .feature-list li span * {
  color: #ffffff !important;
  font-size: 0.98rem !important;
  font-weight: 600 !important;

}
body .feature-list li strong {
  color: #00f2fe !important;
  font-weight: 800 !important;

}
body .check-icon {
  width: 22px !important;
  height: 22px !important;
  min-width: 22px !important;
  background: #00f2fe !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 0 10px rgba(0, 242, 254, 0.5) !important;

}
body .check-icon::after {
  content: "✓" !important;
  color: #0b132b !important;
  font-weight: 900 !important;
  font-size: 13px !important;

}
</style>"""

# Remove old style tag if present
if '<style id="showcase-contrast-fix">' in content:
    old_start = content.find('<style id="showcase-contrast-fix">')
    old_end = content.find('</style>', old_start) + 8
    content = content[:old_start] + content[old_end:]

content = content.replace('</head>', showcase_override + '\n</head>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Showcase contrast fix applied to index.html!")
