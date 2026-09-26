with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print('LEN OF APP.JS:', len(js))
print('MATCH 1 (31068):', js[31068:31400])
print('MATCH 2 (32551):', js[32551:32900])
