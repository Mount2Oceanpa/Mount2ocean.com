import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = 0

# Fix all "function {" that are missing () - anonymous function declarations
before = content
content = re.sub(r'function\s+\{', 'function() {', content)
if content != before:
    print('Fixed: all anonymous function { -> function() {')
    fixes += 1

# Fix any remaining .trim without ()
before = content
content = re.sub(r'\.trim\.', '.trim().', content)
if content != before:
    print('Fixed: .trim. -> .trim().')
    fixes += 1

# Fix .toLowerCase without ()
before = content
content = re.sub(r'\.toLowerCase\s*:', '.toLowerCase() :', content)
if content != before:
    print('Fixed: .toLowerCase missing ()')
    fixes += 1

# Fix .toUpperCase without ()
before = content
content = re.sub(r'\.toUpperCase([^(\s])', lambda m: '.toUpperCase()' + m.group(1), content)
if content != before:
    print('Fixed: .toUpperCase() calls')
    fixes += 1

# Fix Date.now without ()
before = content
content = re.sub(r'Date\.now([^(])', lambda m: 'Date.now()' + m.group(1), content)
if content != before:
    print('Fixed: Date.now() calls')
    fixes += 1

# Fix new Date. without ()
before = content
content = re.sub(r'new Date\.', 'new Date().', content)
if content != before:
    print('Fixed: new Date. -> new Date().')
    fixes += 1

# Fix window.collectAndStoreUser check
before = content
content = re.sub(r'collectAndStoreUser\)', 'collectAndStoreUser)', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total fixes: ' + str(fixes))
print('File size: ' + str(len(content)))
