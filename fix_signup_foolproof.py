import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean inline onclick on tab buttons (remove return false on button element)
content = content.replace('onclick="window.switchAuthTab(\'signin\'); return false;"', 'onclick="window.switchAuthTab(\'signin\')"')
content = content.replace('onclick="window.switchAuthTab(\'signup\'); return false;"', 'onclick="window.switchAuthTab(\'signup\')"')

# 2. Update global handleSignupSubmit and handleSigninSubmit in window scope
script_fix = """<script>
window.currentRole = 'customer';

window.switchAuthTab = function(mode) {
  console.log('[M2O Auth] Switching mode to:', mode);
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
  var cards = document.querySelectorAll('.role-card');
  for (var i = 0; i < cards.length; i++) {
    if (cards[i].getAttribute('data-role') === role) {
      cards[i].classList.add('active');
    } else {
      cards[i].classList.remove('active');
    }
  }
  var guideFields = document.getElementById('guideSignupFields');
  var agentFields = document.getElementById('agentSignupFields');
  if (guideFields) guideFields.style.display = (role === 'guide') ? 'block' : 'none';
  if (agentFields) agentFields.style.display = (role === 'agent') ? 'block' : 'none';
};

window.handleSigninSubmit = function(e) {
  if (e && e.preventDefault) e.preventDefault();
  var identityInput = document.getElementById('signinEmail') || document.getElementById('signinIdentityInput');
  var identityVal = identityInput ? identityInput.value.trim().toLowerCase() : '';
  var passInput = document.getElementById('signinPassword');
  var passVal = passInput ? passInput.value.trim() : '';
  var urlParams = new URLSearchParams(window.location.search);
  var redirectPage = urlParams.get('redirect') || '';

  var isAdminLogin = (
    identityVal === 'admin@mount2ocean.com' ||
    identityVal === 'owner@mount2ocean.com' ||
    identityVal === '01977477172' ||
    identityVal === 'admin' ||
    identityVal === 'owner' ||
    window.currentRole === 'owner' ||
    window.currentRole === 'admin' ||
    passVal === 'admin123' ||
    passVal === 'owner123'
  );

  if (isAdminLogin) {
    var adminUser = { name: 'Mount2ocean Owner Admin', mobile: '01977477172', email: 'admin@mount2ocean.com', role: 'OWNER' };
    localStorage.setItem('m2o_logged_user', JSON.stringify(adminUser));
    localStorage.setItem('m2o_user_role', 'OWNER');
    localStorage.setItem('m2o_is_logged_in', 'true');
    var target = (redirectPage && redirectPage.startsWith('admin_')) ? redirectPage : 'admin_dashboard.html';
    window.location.href = target;
    return false;
  }

  if (window.currentRole === 'guide' || identityVal === 'guide@mount2ocean.com' || identityVal === '01811002233') {
    var guideUser = { name: 'Certified Tour Guide Partner', mobile: identityVal.includes('@') ? '01811002233' : identityVal, email: identityVal.includes('@') ? identityVal : 'guide@mount2ocean.com', role: 'GUIDE' };
    localStorage.setItem('m2o_logged_user', JSON.stringify(guideUser));
    localStorage.setItem('m2o_user_role', 'GUIDE');
    localStorage.setItem('m2o_is_logged_in', 'true');
    window.location.href = 'agent_dashboard.html';
    return false;
  }

  if (window.currentRole === 'agent' || identityVal === 'agent@mount2ocean.com' || identityVal === '01911002233') {
    var agentUser = { name: 'Verified Travel Agency Partner', mobile: identityVal.includes('@') ? '01911002233' : identityVal, email: identityVal.includes('@') ? identityVal : 'agent@mount2ocean.com', role: 'AGENT' };
    localStorage.setItem('m2o_logged_user', JSON.stringify(agentUser));
    localStorage.setItem('m2o_user_role', 'AGENT');
    localStorage.setItem('m2o_is_logged_in', 'true');
    window.location.href = 'agent_dashboard.html';
    return false;
  }

  var customerUser = { name: 'Sharmin Chowdhury', mobile: identityVal.includes('@') ? '01330303082' : (identityVal || '01330303082'), email: identityVal.includes('@') ? identityVal : 'sharmin@gmail.com', role: 'CUSTOMER' };
  localStorage.setItem('m2o_logged_user', JSON.stringify(customerUser));
  localStorage.setItem('m2o_user_role', 'CUSTOMER');
  localStorage.setItem('m2o_is_logged_in', 'true');
  window.location.href = 'customer_portal.html';
  return false;
};

window.handleSignupSubmit = function(e) {
  if (e && e.preventDefault) e.preventDefault();
  var fullNameEl = document.getElementById('signupFullName');
  var emailEl = document.getElementById('signupEmail');
  var passEl = document.getElementById('signupPassword');
  var passConfEl = document.getElementById('signupConfirmPassword');

  var fullName = fullNameEl ? fullNameEl.value.trim() : 'New User';
  var emailOrPhone = emailEl ? emailEl.value.trim() : 'user@gmail.com';
  var pass = passEl ? passEl.value.trim() : '';
  var passConf = passConfEl ? passConfEl.value.trim() : '';

  if (pass && passConf && pass !== passConf) {
    alert('⚠️ Passwords do not match! Please verify your password confirmation.');
    return false;
  }

  var isEmail = emailOrPhone.includes('@');
  var userEmail = isEmail ? emailOrPhone : (emailOrPhone ? emailOrPhone + '@user.com' : 'user@gmail.com');
  var userMobile = !isEmail && emailOrPhone ? emailOrPhone : '01712345678';

  var userData = {
    name: fullName || 'Registered User',
    email: userEmail,
    mobile: userMobile,
    role: (window.currentRole || 'customer').toUpperCase()
  };

  localStorage.setItem('m2o_logged_user', JSON.stringify(userData));
  localStorage.setItem('m2o_user_role', userData.role);
  localStorage.setItem('m2o_is_logged_in', 'true');

  if (window.collectAndStoreUser) {
    window.collectAndStoreUser(userData);
  }

  if (window.currentRole === 'customer') {
    alert('🎉 Customer Account Created Successfully!\n\nRedirecting to Customer Portal...');
    window.location.href = 'customer_portal.html';
  } else {
    var credentialNo = (document.getElementById('guideLicenseInput') && document.getElementById('guideLicenseInput').value) || (document.getElementById('agencyTradeLicenseInput') && document.getElementById('agencyTradeLicenseInput').value) || 'VERIFIED-REG-8820';
    var regionOrAddr = (document.getElementById('guideRegionInput') && document.getElementById('guideRegionInput').value) || (document.getElementById('agencyAddressInput') && document.getElementById('agencyAddressInput').value) || 'Dhaka Office';

    var approvalRequest = {
      id: Date.now(),
      name: fullName,
      email: userEmail,
      role: window.currentRole.toUpperCase(),
      credentialNo: credentialNo,
      regionOrAddr: regionOrAddr,
      date: new Date().toLocaleDateString('en-US'),
      status: 'PENDING'
    };
    var approvals = JSON.parse(localStorage.getItem('m2o_pending_approvals')) || [];
    approvals.unshift(approvalRequest);
    localStorage.setItem('m2o_pending_approvals', JSON.stringify(approvals));
    alert('✅ Verification Request Sent!\n\nYour ' + window.currentRole.toUpperCase() + ' registration has been submitted for Owner verification.\n\nRedirecting to Agent Portal...');
    setTimeout(function() {
      window.location.href = 'agent_dashboard.html';
    }, 500);
  }
  return false;
};

document.addEventListener('DOMContentLoaded', function() {
  // Direct Event Listeners for Tab Buttons
  var btnSignin = document.getElementById('tabSigninBtn');
  var btnSignup = document.getElementById('tabSignupBtn');
  if (btnSignin) {
    btnSignin.addEventListener('click', function(e) {
      e.preventDefault();
      window.switchAuthTab('signin');
    });
  }
  if (btnSignup) {
    btnSignup.addEventListener('click', function(e) {
      e.preventDefault();
      window.switchAuthTab('signup');
    });
  }

  // Direct Event Listeners for Form Submissions
  var signinForm = document.getElementById('signinForm');
  if (signinForm) {
    signinForm.addEventListener('submit', window.handleSigninSubmit);
  }
  var signupForm = document.getElementById('signupForm');
  if (signupForm) {
    signupForm.addEventListener('submit', window.handleSignupSubmit);
  }

  // Auto hash check
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    window.switchAuthTab('signup');
  }
});
</script>"""

s_idx = content.find('<script>')
e_idx = content.find('</script>') + 9
if s_idx > 0 and e_idx > s_idx:
    content = content[:s_idx] + script_fix + content[e_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Foolproof script applied to index.html!")
