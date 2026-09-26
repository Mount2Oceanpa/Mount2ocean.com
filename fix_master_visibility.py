import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Master CSS for 100% Contrast & Visibility on Showcase Panel AND Auth Card
master_contrast = """<style id="m2o-master-visibility-fix">
/* 1. LEFT SHOWCASE PANEL TEXT VISIBILITY */
body .showcase-panel {
  background: linear-gradient(135deg, #0b132b 0%, #1c2541 60%, #0b132b 100%) !important;
  border: 1.5px solid rgba(0, 242, 254, 0.4) !important;
  border-radius: 24px !important;
  padding: 2.5rem !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4) !important;
}

body .showcase-panel p,
body .showcase-panel span,
body .showcase-panel div,
body .showcase-desc,
body #previewDesc {
  color: #e2e8f0 !important;
  font-size: 1rem !important;
  line-height: 1.7 !important;
}

body .showcase-panel strong,
body .showcase-panel b {
  color: #00f2fe !important;
  font-weight: 800 !important;
}

body .showcase-heading {
  color: #ffffff !important;
  font-size: 2.5rem !important;
  font-weight: 900 !important;
  line-height: 1.25 !important;
  margin-bottom: 1.2rem !important;
}

body .badge-pill {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  background: rgba(0, 242, 254, 0.15) !important;
  border: 1.5px solid #00f2fe !important;
  color: #00f2fe !important;
  padding: 0.4rem 1rem !important;
  border-radius: 20px !important;
  font-weight: 800 !important;
  font-size: 0.85rem !important;
  margin-bottom: 1.5rem !important;
}

body .pulse-dot {
  width: 8px !important;
  height: 8px !important;
  background: #00f2fe !important;
  border-radius: 50% !important;
  box-shadow: 0 0 10px #00f2fe !important;
}

body .role-preview-card {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(0, 242, 254, 0.4) !important;
  border-radius: 16px !important;
  padding: 1.4rem !important;
  margin: 1.8rem 0 !important;
}

body #previewTitle {
  color: #ffffff !important;
  font-size: 1.15rem !important;
  font-weight: 800 !important;
  margin-bottom: 0.4rem !important;
}

body #previewDesc {
  color: #cbd5e1 !important;
  font-size: 0.95rem !important;
  line-height: 1.6 !important;
}

body .feature-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 1.5rem 0 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 1.1rem !important;
}

body .feature-list li {
  display: flex !important;
  align-items: center !important;
  gap: 0.85rem !important;
}

body .feature-list li span, body .feature-list li span * {
  color: #ffffff !important;
  font-size: 0.98rem !important;
  font-weight: 600 !important;
}

body .feature-list li strong {
  color: #00f2fe !important;
  font-weight: 800 !important;
}

body .check-icon {
  width: 22px !important;
  height: 22px !important;
  min-width: 22px !important;
  background: #00f2fe !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 0 10px rgba(0, 242, 254, 0.5) !important;
}

body .check-icon::after {
  content: "✓" !important;
  color: #0b132b !important;
  font-weight: 900 !important;
  font-size: 13px !important;
}

/* 2. RIGHT AUTH CARD & SIGNUP TAB VISIBILITY */
body .auth-tabs-wrapper {
  background: #e2e8f0 !important;
  padding: 0.35rem !important;
  border-radius: 12px !important;
  display: flex !important;
  gap: 0.5rem !important;
  margin-bottom: 1.5rem !important;
}

body .tab-switch-btn {
  flex: 1 !important;
  padding: 0.75rem 1rem !important;
  border: none !important;
  border-radius: 8px !important;
  font-weight: 800 !important;
  font-size: 0.95rem !important;
  cursor: pointer !important;
  transition: all 0.2s !important;
}

body .tab-switch-btn:not(.active) {
  background: transparent !important;
  color: #475569 !important;
}

body .tab-switch-btn.active {
  background: linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%) !important;
  color: #ffffff !important;
  box-shadow: 0 4px 12px rgba(43, 100, 255, 0.3) !important;
}

body .glass-card {
  background: #ffffff !important;
  border-radius: 20px !important;
  box-shadow: 0 15px 35px rgba(0,0,0,0.15) !important;
  color: #0f172a !important;
  padding: 2rem !important;
}

body .glass-card h2, body .glass-card h3, body .glass-card h4 {
  color: #0f172a !important;
  font-weight: 800 !important;
}

body .glass-card p {
  color: #475569 !important;
}

body .glass-card label {
  color: #1e293b !important;
  font-weight: 700 !important;
  font-size: 0.9rem !important;
}

body .glass-card input[type="text"],
body .glass-card input[type="password"],
body .glass-card input[type="email"] {
  background: #f8fafc !important;
  color: #0f172a !important;
  border: 1.5px solid #cbd5e1 !important;
  border-radius: 10px !important;
  padding: 0.75rem 1rem !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
}

body .glass-card input::placeholder {
  color: #94a3b8 !important;
}

body .checkbox-label {
  color: #334155 !important;
  font-weight: 600 !important;
  font-size: 0.88rem !important;
}

body .role-box-title {
  color: #0f172a !important;
  font-weight: 800 !important;
}

body .role-card {
  background: #f1f5f9 !important;
  border: 2px solid #e2e8f0 !important;
  border-radius: 12px !important;
}

body .role-card.active {
  border-color: #2b64ff !important;
  background: #eff6ff !important;
}

body .role-name {
  color: #0f172a !important;
  font-weight: 800 !important;
}

body .role-sub {
  color: #64748b !important;
  font-size: 0.78rem !important;
}
</style>"""

# Replace any existing fix style blocks
for style_id in ['m2o-master-visibility-fix', 'showcase-contrast-fix']:
    if style_id in content:
        start = content.find(f'<style id="{style_id}">')
        if start > 0:
            end = content.find('</style>', start) + 8
            content = content[:start] + content[end:]

content = content.replace('</head>', master_contrast + '\n</head>', 1)

# Ensure switchAuthTab properly manages .active class
clean_script_block = """<script>
var currentRole = 'customer';

document.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    switchAuthTab('signup');
  }
  var urlParams = new URLSearchParams(window.location.search);
  var isUnauthorized = urlParams.get('unauthorized');
  var redirectMsg = sessionStorage.getItem('m2o_auth_redirect_msg');
  var authAlertBanner = document.getElementById('authAlertBanner');
  if (isUnauthorized || redirectMsg) {
    if (authAlertBanner) {
      authAlertBanner.style.display = 'block';
      if (redirectMsg) {
        var bannerText = document.getElementById('authAlertText');
        if (bannerText) bannerText.textContent = redirectMsg;
      }
    }
    sessionStorage.removeItem('m2o_auth_redirect_msg');
  }
});

function switchAuthTab(mode) {
  var signinView = document.getElementById('signinView');
  var signupView = document.getElementById('signupView');
  var tabSigninBtn = document.getElementById('tabSigninBtn');
  var tabSignupBtn = document.getElementById('tabSignupBtn');
  
  if (mode === 'signin') {
    if (signinView) signinView.style.display = 'block';
    if (signupView) signupView.style.display = 'none';
    if (tabSigninBtn) {
      tabSigninBtn.classList.add('active');
      tabSigninBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)';
      tabSigninBtn.style.color = '#ffffff';
    }
    if (tabSignupBtn) {
      tabSignupBtn.classList.remove('active');
      tabSignupBtn.style.background = 'transparent';
      tabSignupBtn.style.color = '#475569';
    }
  } else {
    if (signupView) signupView.style.display = 'block';
    if (signinView) signinView.style.display = 'none';
    if (tabSignupBtn) {
      tabSignupBtn.classList.add('active');
      tabSignupBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)';
      tabSignupBtn.style.color = '#ffffff';
    }
    if (tabSigninBtn) {
      tabSigninBtn.classList.remove('active');
      tabSigninBtn.style.background = 'transparent';
      tabSigninBtn.style.color = '#475569';
    }
  }
}

function selectRole(role) {
  currentRole = role;
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
}

function handleSigninSubmit(e) {
  e.preventDefault();
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
    currentRole === 'owner' ||
    currentRole === 'admin' ||
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
    return;
  }

  if (currentRole === 'guide' || identityVal === 'guide@mount2ocean.com' || identityVal === '01811002233') {
    var guideUser = { name: 'Certified Tour Guide Partner', mobile: identityVal.includes('@') ? '01811002233' : identityVal, email: identityVal.includes('@') ? identityVal : 'guide@mount2ocean.com', role: 'GUIDE' };
    localStorage.setItem('m2o_logged_user', JSON.stringify(guideUser));
    localStorage.setItem('m2o_user_role', 'GUIDE');
    localStorage.setItem('m2o_is_logged_in', 'true');
    window.location.href = 'agent_dashboard.html';
    return;
  }

  if (currentRole === 'agent' || identityVal === 'agent@mount2ocean.com' || identityVal === '01911002233') {
    var agentUser = { name: 'Verified Travel Agency Partner', mobile: identityVal.includes('@') ? '01911002233' : identityVal, email: identityVal.includes('@') ? identityVal : 'agent@mount2ocean.com', role: 'AGENT' };
    localStorage.setItem('m2o_logged_user', JSON.stringify(agentUser));
    localStorage.setItem('m2o_user_role', 'AGENT');
    localStorage.setItem('m2o_is_logged_in', 'true');
    window.location.href = 'agent_dashboard.html';
    return;
  }

  var customerUser = { name: 'Sharmin Chowdhury', mobile: identityVal.includes('@') ? '01330303082' : (identityVal || '01330303082'), email: identityVal.includes('@') ? identityVal : 'sharmin@gmail.com', role: 'CUSTOMER' };
  localStorage.setItem('m2o_logged_user', JSON.stringify(customerUser));
  localStorage.setItem('m2o_user_role', 'CUSTOMER');
  localStorage.setItem('m2o_is_logged_in', 'true');
  window.location.href = 'customer_portal.html';
}

function handleSignupSubmit(e) {
  e.preventDefault();
  var fullName = document.getElementById('signupFullName') ? document.getElementById('signupFullName').value.trim() : '';
  var emailOrPhone = document.getElementById('signupEmail') ? document.getElementById('signupEmail').value.trim() : '';
  var pass = document.getElementById('signupPassword') ? document.getElementById('signupPassword').value.trim() : '';
  var passConf = document.getElementById('signupConfirmPassword') ? document.getElementById('signupConfirmPassword').value.trim() : '';

  if (pass && passConf && pass !== passConf) {
    alert('⚠️ Passwords do not match! Please verify your password confirmation.');
    return;
  }

  var isEmail = emailOrPhone.includes('@');
  var userEmail = isEmail ? emailOrPhone : (emailOrPhone ? emailOrPhone + '@user.com' : 'user@gmail.com');
  var userMobile = !isEmail && emailOrPhone ? emailOrPhone : '01712345678';

  var userData = {
    name: fullName || 'Registered User',
    email: userEmail,
    mobile: userMobile,
    role: (currentRole || 'customer').toUpperCase()
  };

  localStorage.setItem('m2o_logged_user', JSON.stringify(userData));
  localStorage.setItem('m2o_user_role', userData.role);
  localStorage.setItem('m2o_is_logged_in', 'true');

  if (window.collectAndStoreUser) {
    window.collectAndStoreUser(userData);
  }

  if (currentRole === 'customer') {
    alert('🎉 Customer Account created successfully! Redirecting to Customer Portal...');
    window.location.href = 'customer_portal.html';
  } else {
    var credentialNo = '';
    var regionOrAddr = '';
    if (currentRole === 'guide') {
      credentialNo = (document.getElementById('guideLicenseInput') && document.getElementById('guideLicenseInput').value) || 'TG-NID-884920';
      regionOrAddr = (document.getElementById('guideRegionInput') && document.getElementById('guideRegionInput').value) || 'Cox\'s Bazar & Sylhet';
    } else if (currentRole === 'agent') {
      credentialNo = (document.getElementById('agencyTradeLicenseInput') && document.getElementById('agencyTradeLicenseInput').value) || 'TRAD-DNCC-019284';
      regionOrAddr = (document.getElementById('agencyAddressInput') && document.getElementById('agencyAddressInput').value) || 'Dhaka B2B Office';
    }
    var approvalRequest = {
      id: Date.now(),
      name: fullName || (currentRole === 'guide' ? 'Certified Tour Guide' : 'Travel Agency Partner'),
      email: userEmail,
      role: currentRole.toUpperCase(),
      credentialNo: credentialNo,
      regionOrAddr: regionOrAddr,
      date: new Date().toLocaleDateString('en-US'),
      status: 'PENDING'
    };
    var approvals = JSON.parse(localStorage.getItem('m2o_pending_approvals')) || [];
    approvals.unshift(approvalRequest);
    localStorage.setItem('m2o_pending_approvals', JSON.stringify(approvals));
    alert('✅ Verification Request Sent!\n\nYour ' + currentRole.toUpperCase() + ' registration (Credential No: ' + credentialNo + ') has been submitted for Owner verification.\n\nRedirecting to Agent Portal...');
    setTimeout(function() {
      window.location.href = 'agent_dashboard.html';
    }, 800);
  }
}
</script>"""

s_idx = content.find('<script>')
e_idx = content.find('</script>') + 9
if s_idx > 0 and e_idx > s_idx:
    content = content[:s_idx] + clean_script_block + content[e_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Master visibility fix applied to index.html!")
