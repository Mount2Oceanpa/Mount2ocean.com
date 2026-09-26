import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add URL hash / query check for #signup on page load in DOMContentLoaded
old_dcl = "document.addEventListener('DOMContentLoaded', function() {"
new_dcl = """document.addEventListener('DOMContentLoaded', function() {
  // Hash or Query param tab auto-switch
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    switchAuthTab('signup');
  }"""

if old_dcl in content and 'window.location.hash === \'#signup\'' not in content:
    content = content.replace(old_dcl, new_dcl, 1)
    print("Added #signup hash listener to DOMContentLoaded")

# 2. Enhance switchAuthTab to handle button active backgrounds properly
old_switch = """function switchAuthTab(mode) { var signinView = document.getElementById('signinView'); var signupView = document.getElementById('signupView'); var tabSigninBtn = document.getElementById('tabSigninBtn'); var tabSignupBtn = document.getElementById('tabSignupBtn'); if (mode === 'signin') { if (signinView) signinView.style.display = 'block'; if (signupView) signupView.style.display = 'none'; if (tabSigninBtn) { tabSigninBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)'; tabSigninBtn.style.color = '#ffffff'; } if (tabSignupBtn) { tabSignupBtn.style.background = 'transparent'; tabSignupBtn.style.color = '#94a3b8'; } } else { if (signupView) signupView.style.display = 'block'; if (signinView) signinView.style.display = 'none'; if (tabSignupBtn) { tabSignupBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)'; tabSignupBtn.style.color = '#ffffff'; } if (tabSigninBtn) { tabSigninBtn.style.background = 'transparent'; tabSigninBtn.style.color = '#94a3b8'; } } }"""

new_switch = """function switchAuthTab(mode) {
  var signinView = document.getElementById('signinView');
  var signupView = document.getElementById('signupView');
  var tabSigninBtn = document.getElementById('tabSigninBtn');
  var tabSignupBtn = document.getElementById('tabSignupBtn');
  if (mode === 'signin') {
    if (signinView) signinView.style.display = 'block';
    if (signupView) signupView.style.display = 'none';
    if (tabSigninBtn) {
      tabSigninBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)';
      tabSigninBtn.style.color = '#ffffff';
    }
    if (tabSignupBtn) {
      tabSignupBtn.style.background = 'transparent';
      tabSignupBtn.style.color = '#ffffff';
    }
  } else {
    if (signupView) signupView.style.display = 'block';
    if (signinView) signinView.style.display = 'none';
    if (tabSignupBtn) {
      tabSignupBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)';
      tabSignupBtn.style.color = '#ffffff';
    }
    if (tabSigninBtn) {
      tabSigninBtn.style.background = 'transparent';
      tabSigninBtn.style.color = '#ffffff';
    }
  }
}"""

if old_switch in content:
    content = content.replace(old_switch, new_switch, 1)
    print("Updated switchAuthTab button colors")

# 3. Enhance handleSignupSubmit with password match check & proper field reading
old_signup_func = """function handleSignupSubmit(e) { e.preventDefault(); var fullName = document.getElementById('signupFullName').value || 'New Registered User'; var email = document.getElementById('signupEmail').value || 'new.user@gmail.com'; var mobile = document.getElementById('signupMobileInput') ? document.getElementById('signupMobileInput').value : '01712345678'; var userData = { name: fullName, email: email, mobile: mobile, role: currentRole.toUpperCase() }; if (window.collectAndStoreUser) { window.collectAndStoreUser(userData); } else { localStorage.setItem('m2o_logged_user', JSON.stringify(userData)); } if (currentRole === 'customer') { alert(' Customer Account created successfully! User profile stored in Owner Directory. Redirecting to Customer Portal...'); window.location.href = 'customer_portal.html'; } else { var credentialNo = ''; var regionOrAddr = ''; if (currentRole === 'guide') { credentialNo = document.getElementById('guideLicenseInput').value || 'TG-NID-884920'; regionOrAddr = document.getElementById('guideRegionInput').value || 'Cox\'s Bazar & Sylhet'; } else if (currentRole === 'agent') { credentialNo = document.getElementById('agencyTradeLicenseInput').value || 'TRAD-DNCC-019284'; regionOrAddr = document.getElementById('agencyAddressInput').value || 'Dhaka B2B Office'; } var approvalRequest = { id: Date.now(), name: fullName || (currentRole === 'guide' ? 'Rahman Guide' : 'SkyLine Travel Agency'), email: email || 'partner@mount2ocean.com', role: currentRole.toUpperCase(), credentialNo: credentialNo, regionOrAddr: regionOrAddr, date: new Date().toLocaleDateString('bn-BD'), status: 'PENDING' }; var approvals = JSON.parse(localStorage.getItem('m2o_pending_approvals')) || []; approvals.unshift(approvalRequest); localStorage.setItem('m2o_pending_approvals', JSON.stringify(approvals)); alert(' Verification Request Sent!\\n\\nYour ' + currentRole.toUpperCase() + ' registration (NID/License/Trade No: ' + credentialNo + ') has been submitted to the Mount2ocean Owner Dashboard for verification.\\n\\nOnce approved by Owner Admin, a confirmation email will be dispatched to your email!'); setTimeout(function() { window.location.href = 'agent_dashboard.html'; }, 1000); } }"""

new_signup_func = """function handleSignupSubmit(e) {
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
    alert('🎉 Customer Account created successfully!\n\nWelcome to Mount2ocean Travel & Tours. Redirecting to Customer Portal...');
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
}"""

if old_signup_func in content:
    content = content.replace(old_signup_func, new_signup_func, 1)
    print("Updated handleSignupSubmit function")

# 4. Master CSS Injection for Sign Up / Sign In card contrast
contrast_css = """<style>
/* AUTH CARD & SIGNUP FORM CONTRAST GUARANTEE */
.glass-card { background: #ffffff !important; border-radius: 20px !important; box-shadow: 0 15px 35px rgba(0,0,0,0.15) !important; color: #0f172a !important; padding: 2rem !important; }
.glass-card h2, .glass-card h3, .glass-card h4 { color: #0f172a !important; font-weight: 800 !important; }
.glass-card p { color: #475569 !important; }
.glass-card label { color: #1e293b !important; font-weight: 700 !important; font-size: 0.9rem !important; }
.glass-card input[type="text"], .glass-card input[type="password"], .glass-card input[type="email"] { background: #f8fafc !important; color: #0f172a !important; border: 1.5px solid #cbd5e1 !important; border-radius: 10px !important; padding: 0.75rem 1rem !important; font-size: 0.95rem !important; font-weight: 600 !important; }
.glass-card input::placeholder { color: #94a3b8 !important; }
.glass-card input:focus { border-color: #2b64ff !important; background: #ffffff !important; outline: none !important; box-shadow: 0 0 0 3px rgba(43,100,255,0.15) !important; }
.checkbox-label { color: #334155 !important; font-weight: 600 !important; font-size: 0.88rem !important; }
.role-box-title { color: #0f172a !important; font-weight: 800 !important; }
.role-card { background: #f1f5f9 !important; border: 2px solid #e2e8f0 !important; border-radius: 12px !important; }
.role-card.active { border-color: #2b64ff !important; background: #eff6ff !important; }
.role-name { color: #0f172a !important; font-weight: 800 !important; }
.role-sub { color: #64748b !important; font-size: 0.78rem !important; }
</style>"""

if 'AUTH CARD & SIGNUP FORM CONTRAST GUARANTEE' not in content:
    content = content.replace('</head>', contrast_css + '\n</head>', 1)
    print("Injected signup & glass card contrast CSS")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html update complete!")
