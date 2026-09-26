import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace invalid background: rgba; with background: #f1f5f9;
content = content.replace('background: rgba;', 'background: #f1f5f9;')
content = content.replace('background: rgba', 'background: #f1f5f9')

clean_script = """<script>
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
      tabSigninBtn.style.background = 'linear-gradient(135deg, #2b64ff 0%, #1c52d8 100%)';
      tabSigninBtn.style.color = '#ffffff';
    }
    if (tabSignupBtn) {
      tabSignupBtn.style.background = 'transparent';
      tabSignupBtn.style.color = '#475569';
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

# Replace the first <script> ... </script> block in index.html
s_idx = content.find('<script>')
e_idx = content.find('</script>') + 9

if s_idx > 0 and e_idx > s_idx:
    content = content[:s_idx] + clean_script + content[e_idx:]
    print("Replaced script block cleanly!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html clean script replacement done!")
