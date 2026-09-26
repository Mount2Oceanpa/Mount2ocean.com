import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace switchAuthTab in app.js with window.switchAuthTab
s_idx = js.find('window.switchAuthTab = function')
if s_idx > 0:
    js = js[:s_idx]

app_js_auth_engine = """
// ==========================================
// MOUNT2OCEAN AUTH ENGINE & TAB SWITCHER (FOOLPROOF)
// ==========================================
window.currentRole = window.currentRole || 'customer';

window.switchAuthTab = function(mode) {
  console.log('[M2O Auth app.js] Switching mode to:', mode);
  var signinView = document.getElementById('signinView');
  var signupView = document.getElementById('signupView');
  var tabSigninBtn = document.getElementById('tabSigninBtn');
  var tabSignupBtn = document.getElementById('tabSignupBtn');

  if (mode === 'signup') {
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
    try { history.replaceState(null, null, '#signup'); } catch(e) {}
  } else {
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

document.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    window.switchAuthTab('signup');
  }
  
  var btnSignin = document.getElementById('tabSigninBtn');
  var btnSignup = document.getElementById('tabSignupBtn');
  if (btnSignin) {
    btnSignin.onclick = function(e) { if(e) e.preventDefault(); window.switchAuthTab('signin'); return false; };
  }
  if (btnSignup) {
    btnSignup.onclick = function(e) { if(e) e.preventDefault(); window.switchAuthTab('signup'); return false; };
  }
});

window.addEventListener('hashchange', function() {
  if (window.location.hash === '#signup') {
    window.switchAuthTab('signup');
  } else if (window.location.hash === '#signin') {
    window.switchAuthTab('signin');
  }
});
"""

js += app_js_auth_engine

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js synchronized cleanly!")
