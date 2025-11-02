// SIGNUP FORM
const signupForm = document.getElementById('signupForm');
if (signupForm) {
    signupForm.addEventListener('submit', function (e) {
        e.preventDefault();
        validateSignupForm();
    });
}

function validateSignupForm() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();
    const errorDiv = document.getElementById('signupErrors');
    errorDiv.innerHTML = '';

    let errors = [];

    if (!name) errors.push('Name is required.');
    if (!email) errors.push('Email is required.');
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.push('Invalid email.');
    if (!password) errors.push('Password is required.');
    else if (password.length < 6) errors.push('Password must be at least 6 characters.');
    if (password !== confirmPassword) errors.push('Passwords do not match.');

    if (errors.length > 0) {
        errors.forEach(err => {
            const li = document.createElement('li');
            li.textContent = err;
            errorDiv.appendChild(li);
        });
    } else {
        signupForm.submit();
    }
}

// LOST & FOUND FORM
const lostFoundForm = document.getElementById('lostFoundForm');
if (lostFoundForm) {
    lostFoundForm.addEventListener('submit', function (e) {
        e.preventDefault();
        validateLostFoundForm();
    });
}

function validateLostFoundForm() {
    const itemName = document.getElementById('itemName').value.trim();
    const description = document.getElementById('description').value.trim();
    const date = document.getElementById('dateLostFound').value.trim();
    const contact = document.getElementById('contactInfo').value.trim();
    const errorDiv = document.getElementById('lostFoundErrors');
    errorDiv.innerHTML = '';

    let errors = [];

    if (!itemName) errors.push('Item name is required.');
    if (!description) errors.push('Description is required.');
    if (!date) errors.push('Date is required.');
    if (!contact) errors.push('Contact info is required.');
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contact) && !/^\d{10,15}$/.test(contact)) {
        errors.push('Contact must be a valid email or phone number.');
    }

    if (errors.length > 0) {
        errors.forEach(err => {
            const li = document.createElement('li');
            li.textContent = err;
            errorDiv.appendChild(li);
        });
    } else {
        lostFoundForm.submit();
    }
}
