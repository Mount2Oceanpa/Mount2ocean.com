with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s1 = text.find('id="signinView"')
if s1 > 0:
    print('signinView:', text[s1-30:s1+80])

s2 = text.find('id="signupView"')
if s2 > 0:
    print('signupView:', text[s2-30:s2+80])
