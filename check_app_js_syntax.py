with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

s = js.find('tabSigninBtn.styl')
while s > 0:
    print('--- MATCH AT', s, '---')
    print(js[s-20:s+300])
    s = js.find('tabSigninBtn.styl', s+300)
