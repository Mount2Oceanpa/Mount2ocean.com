import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Showcase Panel HTML with Direct Inline White Styles for 100% Specificity
old_showcase_p = '<p class="showcase-desc"> Seamlessly connect as a <strong>Traveler</strong>, certified <strong>Tour Guide</strong>, or registered <strong>Travel Agent</strong>. Access specialized tools, bookings, and management dashboards tailored to your profile. </p>'

new_showcase_p = '<p class="showcase-desc" style="color: #ffffff !important; font-size: 1.05rem !important; line-height: 1.75 !important; font-weight: 600 !important; margin-bottom: 1.8rem !important; text-shadow: 0 1px 3px rgba(0,0,0,0.5) !important;"> Seamlessly connect as a <strong style="color: #00f2fe !important; font-weight: 900 !important;">Traveler</strong>, certified <strong style="color: #00f2fe !important; font-weight: 900 !important;">Tour Guide</strong>, or registered <strong style="color: #00f2fe !important; font-weight: 900 !important;">Travel Agent</strong>. Access specialized tools, bookings, and management dashboards tailored to your profile. </p>'

if old_showcase_p in content:
    content = content.replace(old_showcase_p, new_showcase_p)
    print("Replaced showcase paragraph with direct inline white styles")

# 2. Update role preview card titles & descriptions inline
old_card_desc = '<p id="previewDesc">Book curated tours, save travel itineraries, track active bookings, and earn loyalty rewards.</p>'
new_card_desc = '<p id="previewDesc" style="color: #ffffff !important; font-size: 0.95rem !important; line-height: 1.6 !important; font-weight: 600 !important; margin: 0 !important; text-shadow: 0 1px 2px rgba(0,0,0,0.4) !important;">Book curated tours, save travel itineraries, track active bookings, and earn loyalty rewards.</p>'

if old_card_desc in content:
    content = content.replace(old_card_desc, new_card_desc)
    print("Replaced previewDesc with direct inline white styles")

old_card_title = '<h4 id="previewTitle">Customer Account Features</h4>'
new_card_title = '<h4 id="previewTitle" style="color: #ffffff !important; font-weight: 900 !important; font-size: 1.15rem !important; margin-bottom: 0.4rem !important;">Customer Account Features</h4>'

if old_card_title in content:
    content = content.replace(old_card_title, new_card_title)
    print("Replaced previewTitle with direct inline white styles")

# 3. Update feature list bullets inline
old_bullets = """<ul class="feature-list"> <li> <span class="check-icon"></span> <span><strong>Unified Security:</strong> Multi-factor authentication & role permissions</span> </li> <li> <span class="check-icon"></span> <span><strong>Instant Switching:</strong> One-click selection between Customer, Guide & Agent</span> </li> <li> <span class="check-icon"></span> <span><strong>Password Recovery:</strong> OTP verification modal integrated</span> </li> </ul>"""

new_bullets = """<ul class="feature-list" style="list-style: none !important; padding: 0 !important; margin: 1.5rem 0 0 !important; display: flex !important; flex-direction: column !important; gap: 1.1rem !important;">
  <li style="display: flex !important; align-items: center !important; gap: 0.85rem !important;">
    <span class="check-icon" style="width: 22px !important; height: 22px !important; min-width: 22px !important; background: #00f2fe !important; border-radius: 50% !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; color: #0b132b !important; font-weight: 900 !important; font-size: 13px !important;">✓</span>
    <span style="color: #ffffff !important; font-size: 0.98rem !important; font-weight: 600 !important;"><strong style="color: #00f2fe !important; font-weight: 900 !important;">Unified Security:</strong> Multi-factor authentication &amp; role permissions</span>
  </li>
  <li style="display: flex !important; align-items: center !important; gap: 0.85rem !important;">
    <span class="check-icon" style="width: 22px !important; height: 22px !important; min-width: 22px !important; background: #00f2fe !important; border-radius: 50% !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; color: #0b132b !important; font-weight: 900 !important; font-size: 13px !important;">✓</span>
    <span style="color: #ffffff !important; font-size: 0.98rem !important; font-weight: 600 !important;"><strong style="color: #00f2fe !important; font-weight: 900 !important;">Instant Switching:</strong> One-click selection between Customer, Guide &amp; Agent</span>
  </li>
  <li style="display: flex !important; align-items: center !important; gap: 0.85rem !important;">
    <span class="check-icon" style="width: 22px !important; height: 22px !important; min-width: 22px !important; background: #00f2fe !important; border-radius: 50% !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; color: #0b132b !important; font-weight: 900 !important; font-size: 13px !important;">✓</span>
    <span style="color: #ffffff !important; font-size: 0.98rem !important; font-weight: 600 !important;"><strong style="color: #00f2fe !important; font-weight: 900 !important;">Password Recovery:</strong> OTP verification modal integrated</span>
  </li>
</ul>"""

if old_bullets in content:
    content = content.replace(old_bullets, new_bullets)
    print("Replaced feature bullets with direct inline white styles")

# 4. Update JavaScript for robust tab switching & event listeners
bulletproof_script = """<script>
var currentRole = 'customer';

document.addEventListener('DOMContentLoaded', function() {
  // Check hash or query parameter
  if (window.location.hash === '#signup' || window.location.search.includes('mode=signup')) {
    switchAuthTab('signup');
  }

  // Attach explicit click listeners to tab buttons
  var btnSignin = document.getElementById('tabSigninBtn');
  var btnSignup = document.getElementById('tabSignupBtn');
  if (btnSignin) {
    btnSignin.addEventListener('click', function(e) {
      e.preventDefault();
      switchAuthTab('signin');
    });
  }
  if (btnSignup) {
    btnSignup.addEventListener('click', function(e) {
      e.preventDefault();
      switchAuthTab('signup');
    });
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
  } else {
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
    content = content[:s_idx] + bulletproof_script + content[e_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Comprehensive inline styles and JS tab fixes applied to index.html!")
