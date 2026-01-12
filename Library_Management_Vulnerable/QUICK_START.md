# 🚀 QUICK START GUIDE

## Get Started in 5 Minutes!

### Step 1: Open in GitHub Codespaces
1. Fork this repository to your GitHub account
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python3 main.py
```

### Step 4: Open in Browser
- Codespaces will show a popup: "Your application running on port 5000 is available"
- Click "Open in Browser"

### Step 5: Login
Use these test accounts:
- **Username**: alice | **Password**: password123
- **Username**: bob | **Password**: qwerty

---

## 🎯 Your First Security Test

### Test 1: SQL Injection in Login
1. Go to the login page
2. Enter this in the username field: `' OR '1'='1' --`
3. Enter anything in the password field
4. Click "Login"
5. **Result**: You should be logged in without a valid password!

### Test 2: XSS in Reviews
1. Login with a test account
2. Go to "Reviews" page
3. Enter a book title: `Test Book`
4. Enter this review: `<script>alert('XSS Attack!')</script>`
5. Click "Submit Review"
6. **Result**: An alert box should appear!

### Test 3: IDOR in Dashboard
1. Login as alice
2. Go to "My Books" (dashboard)
3. Change the URL to: `/dashboard.html?id=2`
4. **Result**: You can see bob's borrowed books!

---

## 📋 What to Do Next

1. **Document** each vulnerability you find
2. **Fix** the vulnerability using secure coding
3. **Test** that your fix works
4. **Commit** your changes with clear messages
5. **Repeat** for all vulnerabilities

---

## 💡 Pro Tips

- Use the hints in the application (yellow boxes)
- Check the `.student_resources/` folder for examples
- Test each fix thoroughly before moving to the next
- Keep notes as you go - you'll need them for your report

---

## 🆘 Troubleshooting

**Problem**: Application won't start
- **Solution**: Make sure you ran `pip install -r requirements.txt`

**Problem**: Database error
- **Solution**: Delete `database_files/library.db` and restart the app

**Problem**: Can't see vulnerabilities
- **Solution**: Look for f-strings in Python files and `|safe` in HTML templates

---

**Ready? Start your security audit now!** 🔍
