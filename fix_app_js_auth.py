import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace switchAuthTab function in app.js
old_func_start = js.find('switchAuthTab = function(mode)')
if old_func_start == -1:
    old_func_start = js.find('window.switchAuthTab = function(mode)')

if old_func_start > 0:
    old_func_end = js.find('window.selectRole = function', old_func_start)
    if old_func_end > old_func_start:
        old_block = js[old_func_start:old_func_end]
        
        new_block = """window.switchAuthTab = function(mode) {
  const signinView = document.getElementById('signinView');
  const signupView = document.getElementById('signupView');
  const tabSigninBtn = document.getElementById('tabSigninBtn');
  const tabSignupBtn = document.getElementById('tabSignupBtn');

  if (mode === 'signin') {
    if (signinView) signinView.style.setProperty('display', 'block', 'important');
    if (signupView) signupView.style.setProperty('display', 'none', 'important');

    if (tabSigninBtn) {
      tabSigninBtn.classList.add('active');
      tabSigninBtn.style.setProperty('background', 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)', 'important');
      tabSigninBtn.style.setProperty('color', '#ffffff', 'important');
    }
    if (tabSignupBtn) {
      tabSignupBtn.classList.remove('active');
      tabSignupBtn.style.setProperty('background', 'transparent', 'important');
      tabSignupBtn.style.setProperty('color', '#475569', 'important');
    }
  } else {
    if (signupView) signupView.style.setProperty('display', 'block', 'important');
    if (signinView) signinView.style.setProperty('display', 'none', 'important');

    if (tabSignupBtn) {
      tabSignupBtn.classList.add('active');
      tabSignupBtn.style.setProperty('background', 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)', 'important');
      tabSignupBtn.style.setProperty('color', '#ffffff', 'important');
    }
    if (tabSigninBtn) {
      tabSigninBtn.classList.remove('active');
      tabSigninBtn.style.setProperty('background', 'transparent', 'important');
      tabSigninBtn.style.setProperty('color', '#475569', 'important');
    }
  }
};

// Hash & Query auto switcher on page load and hash change
document.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    window.switchAuthTab('signup');
  }
});

window.addEventListener('hashchange', function() {
  if (window.location.hash === '#signup') {
    window.switchAuthTab('signup');
  } else if (window.location.hash === '#signin') {
    window.switchAuthTab('signin');
  }
});

// Run immediate check if script executes after DOMReady
if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
  setTimeout(function() { window.switchAuthTab('signup'); }, 50);
}

"""
        js = js[:old_func_start] + new_block + js[old_func_end:]
        print("Successfully updated switchAuthTab in app.js!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js updated!")
