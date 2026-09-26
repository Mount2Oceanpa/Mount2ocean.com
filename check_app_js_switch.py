with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

s = js.find('switchAuthTab')
while s > 0:
    print('--- MATCH AT', s, '---')
    print(js[s:s+400])
    s = js.find('switchAuthTab', s+400)
