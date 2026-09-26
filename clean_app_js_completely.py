import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove all legacy occurrences of switchAuthTab in app.js
# Search for switchAuthTab = function ... and replace with empty space
js_clean = re.sub(r'(window\.)?switchAuthTab\s*=\s*function[\s\S]*?\}\s*;', '', js)

# 2. Append ONE single clean implementation at the very end of app.js
single_clean_auth = """

// ==========================================
// MOUNT2OCEAN AUTH & TAB SWITCHER ENGINE (ULTRA-RELIABLE)
// ==========================================
window.currentRole = 'customer';

window.switchAuthTab = function(mode) {
  var signinView = document.getElementById('signinView');
  var signupView = document.getElementById('signupView');
  var tabSigninBtn = document.getElementById('tabSigninBtn');
  var tabSignupBtn = document.getElementById('tabSignupBtn');

  if (mode === 'signup') {
    if (signupView) {
      signupView.style.setProperty('display', 'block', 'important');
    }
    if (signinView) {
      signinView.style.setProperty('display', 'none', 'important');
    }
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
    try { history.replaceState(null, null, '#signup'); } catch(e) {}
  } else {
    if (signinView) {
      signinView.style.setProperty('display', 'block', 'important');
    }
    if (signupView) {
      signupView.style.setProperty('display', 'none', 'important');
    }
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
    try { history.replaceState(null, null, '#signin'); } catch(e) {}
  }
};

window.selectRole = function(role) {
  window.currentRole = role;
  document.querySelectorAll('.role-card').forEach(function(card) {
    if (card.getAttribute('data-role') === role) {
      card.classList.add('active');
    } else {
      card.classList.remove('active');
    }
  });
  var guideFields = document.getElementById('guideSignupFields');
  var agentFields = document.getElementById('agentSignupFields');
  if (guideFields) guideFields.style.display = (role === 'guide') ? 'block' : 'none';
  if (agentFields) agentFields.style.display = (role === 'agent') ? 'block' : 'none';
};

// Immediate & DOMReady check for URL hash / query
document.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    window.switchAuthTab('signup');
  }
  
  // Attach direct click handlers to buttons
  var btnSignin = document.getElementById('tabSigninBtn');
  var btnSignup = document.getElementById('tabSignupBtn');
  if (btnSignin) {
    btnSignin.onclick = function(e) { e.preventDefault(); window.switchAuthTab('signin'); };
  }
  if (btnSignup) {
    btnSignup.onclick = function(e) { e.preventDefault(); window.switchAuthTab('signup'); };
  }
});

window.addEventListener('hashchange', function() {
  if (window.location.hash === '#signup') {
    window.switchAuthTab('signup');
  } else if (window.location.hash === '#signin') {
    window.switchAuthTab('signin');
  }
});

if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
  setTimeout(function() { window.switchAuthTab('signup'); }, 50);
}
"""

js_clean += single_clean_auth

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_clean)

print("Cleaned all duplicate switchAuthTab definitions and appended clean auth engine to app.js!")
