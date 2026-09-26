import sys, re
sys.stdout.reconfigure(encoding='utf-8')

print("=== CREATING STANDALONE DEDICATED SIGNUP.HTML PAGE ===")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build signup.html content based on index.html structure
signup_html = content

# Set title
signup_html = signup_html.replace('<title>Mount2ocean | Multi-Role Authentication Portal</title>', '<title>Mount2ocean | Create Free Account</title>')

# Make signup tab active in the switcher
old_tabs = """<div class="auth-tabs-wrapper" style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem; background: #f1f5f9; padding: 0.35rem; border-radius: 12px;"> <button type="button" class="tab-switch-btn active" id="tabSigninBtn" onclick="window.switchAuthTab('signin')" style="flex: 1; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%); color: #ffffff;"> Sign In </button> <button type="button" class="tab-switch-btn" id="tabSignupBtn" onclick="window.switchAuthTab('signup')" style="flex: 1; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: transparent; color: #ffffff;"> Sign Up </button> </div>"""

new_tabs = """<div class="auth-tabs-wrapper" style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem; background: #f1f5f9; padding: 0.35rem; border-radius: 12px;">
  <a href="index.html" class="tab-switch-btn" style="flex: 1; text-align: center; text-decoration: none; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: transparent; color: #475569; display: block;"> Sign In </a>
  <a href="signup.html" class="tab-switch-btn active" style="flex: 1; text-align: center; text-decoration: none; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%); color: #ffffff; display: block; box-shadow: 0 4px 12px rgba(43, 100, 255, 0.3);"> Sign Up </a>
</div>"""

signup_html = signup_html.replace(old_tabs, new_tabs)

# Ensure signupView is display: block by default and signinView is display: none
signup_html = signup_html.replace('<div id="signinView" style="display: block;">', '<div id="signinView" style="display: none;">')
signup_html = signup_html.replace('<div id="signupView" style="display: none;">', '<div id="signupView" style="display: block;">')

with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(signup_html)

print("Created standalone signup.html successfully!")

# Now update index.html tabs to link directly to signup.html
index_tabs_updated = """<div class="auth-tabs-wrapper" style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem; background: #f1f5f9; padding: 0.35rem; border-radius: 12px;">
  <a href="index.html" class="tab-switch-btn active" style="flex: 1; text-align: center; text-decoration: none; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%); color: #ffffff; display: block; box-shadow: 0 4px 12px rgba(43, 100, 255, 0.3);"> Sign In </a>
  <a href="signup.html" class="tab-switch-btn" style="flex: 1; text-align: center; text-decoration: none; padding: 0.75rem 1rem; border: none; border-radius: 8px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; background: transparent; color: #475569; display: block;"> Sign Up </a>
</div>"""

content_index = content.replace(old_tabs, index_tabs_updated)

# Update "Create Free Account" link in index.html to link directly to signup.html
content_index = re.sub(r'<a href="#signup"[^>]*> Create Free Account </a>', '<a href="signup.html" style="color: #00f2fe; font-weight: 700; text-decoration: underline; margin-left: 4px;"> Create Free Account </a>', content_index)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_index)

print("Updated index.html tabs and Create Free Account links to point directly to signup.html!")
