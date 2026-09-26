import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

app_js_tag = '<script src="app.js?v=v51_zero_invisible_contrast"></script>'
failsafe = """<script src="app.js?v=v51_zero_invisible_contrast"></script>
<script>
  // Failsafe auto-switch on page load
  (function() {
    if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
      setTimeout(function() {
        if (window.switchAuthTab) window.switchAuthTab('signup');
      }, 30);
    }
  })();
</script>"""

if app_js_tag in content and 'Failsafe auto-switch on page load' not in content:
    content = content.replace(app_js_tag, failsafe, 1)
    print("Added failsafe script tag after app.js in index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html failsafe check done!")
