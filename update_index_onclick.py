import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update tab switch buttons in index.html to ensure clean inline onclick
content = content.replace('onclick="switchAuthTab(\'signin\')"', 'onclick="window.switchAuthTab(\'signin\'); return false;"')
content = content.replace('onclick="switchAuthTab(\'signup\')"', 'onclick="window.switchAuthTab(\'signup\'); return false;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html button inline onclicks!")
