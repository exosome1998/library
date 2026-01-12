# 📚 CITY LIBRARY MANAGEMENT SYSTEM - SECURITY ASSESSMENT

## ⚠️ EDUCATIONAL PURPOSE ONLY

This is a **security assessment project** for HSC Software Engineering students in Australia.

**DO NOT use this code in production. DO NOT deploy this application publicly.**

---

## 🎯 YOUR TASK

You are a security consultant hired by City Library to audit their new web application. The previous developer has left, and the library is concerned about security vulnerabilities.

### Your Mission:
1. **Find ALL security vulnerabilities** in this application
2. **Fix each vulnerability** using secure coding practices
3. **Test that your fixes work** correctly
4. **Document your findings** in a professional security report

---

## 📖 THE APPLICATION

**City Library Management System** allows members to:
- Login with username and password
- Create new member accounts
- View their borrowed books
- Write and read book reviews
- Access the system as a Progressive Web App (PWA)

---

## 🔍 KNOWN ISSUES

The library has reported:
- Some members claim they can see other members' borrowed books
- Strange HTML and JavaScript code has appeared in book reviews
- The previous developer used "quick and dirty" coding practices
- No security testing has been performed
- Passwords might not be stored securely

---

## 📋 ASSESSMENT STRUCTURE

### **Part 1: Security Audit (40 marks)**

Find and document ALL vulnerabilities in:
- `main.py` (Flask application routes)
- `book_management.py` (Database operations)
- `templates/*.html` (HTML templates)

For each vulnerability, document:
- **What** the vulnerability is (name and type)
- **Where** it is located (file and line number)
- **How** it could be exploited (attack scenario)
- **Impact** of the vulnerability (what damage could occur)

### **Part 2: Fix the Vulnerabilities (40 marks)**

Fix each vulnerability using secure coding practices:
- Use **parameterized queries** for SQL operations
- Implement proper **input validation**
- Use **output encoding** for XSS prevention
- Fix **authentication** and **authorization** issues
- Fix **redirect** vulnerabilities
- Implement **password hashing**

### **Part 3: Testing (10 marks)**

Test that:
- Your fixes **prevent the attacks**
- Normal functionality **still works**
- Document your **testing process** with screenshots

### **Part 4: Security Report (10 marks)**

Write a professional report including:
- **Executive Summary** (1 page)
- **List of vulnerabilities** found with risk ratings
- **Risk assessment** for each vulnerability
- **Fixes implemented** with code examples
- **Testing results** with evidence
- **Recommendations** for future security

---

## 🚀 GETTING STARTED

### **1. Setup**
```bash
# Fork this repository
# Create a GitHub Codespace

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 main.py
```

### **2. Access the Application**
- Open the application in your browser (port 5000)
- Try logging in with test accounts:
  - Username: `alice` / Password: `password123`
  - Username: `bob` / Password: `qwerty`

### **3. Start Your Security Audit**
- Test all forms with malicious input
- Try to access other users' data
- Look for XSS vulnerabilities
- Check for SQL injection points
- Test authentication and authorization

---

## 💡 HINTS

### **Week 1-2: SQL Injection**
- Look for f-strings in SQL queries
- Test login form with: `' OR '1'='1' --`
- Check signup, dashboard, and reviews

### **Week 3: Cross-Site Scripting (XSS)**
- Look for `|safe` filters in templates
- Test review form with: `<script>alert('XSS')</script>`
- Try: `<img src=x onerror="alert('Hacked!')">`

### **Week 4: Authentication & Passwords**
- Check how passwords are stored
- Look for timing attacks in login
- Test password hashing

### **Week 5: CSRF & Redirects**
- Check for CSRF protection
- Test redirect parameter: `/?redirect=https://evil.com`

### **Week 6: Authorization**
- Try accessing other users' data
- Test IDOR: `/dashboard.html?id=2`

---

## 📊 ASSESSMENT CRITERIA

| Grade | Criteria |
|-------|----------|
| **High Distinction (85-100%)** | Found ALL 10+ vulnerabilities, fixed all correctly, comprehensive testing, professional report |
| **Distinction (75-84%)** | Found 8-9 vulnerabilities, fixed most correctly, good testing, clear report |
| **Credit (65-74%)** | Found 6-7 vulnerabilities, fixed most correctly, basic testing, adequate report |
| **Pass (50-64%)** | Found 4-5 vulnerabilities, fixed some correctly, minimal testing, basic report |

---

## 📚 LEARNING OUTCOMES

By completing this assessment, you will learn:
1. **SQL Injection** - How to prevent database attacks
2. **XSS** - How to sanitize user input and output
3. **Authentication** - Secure password storage and timing attacks
4. **Authorization** - Preventing unauthorized access (IDOR)
5. **CSRF** - Cross-Site Request Forgery protection
6. **Open Redirects** - Validating redirect URLs
7. **Security Testing** - SAST and DAST tools
8. **Professional Reporting** - Documenting security findings

---

## 🛠️ TECHNOLOGY STACK

- **Backend**: Python 3.x + Flask
- **Database**: SQLite3
- **Frontend**: HTML5 + CSS3 + JavaScript
- **PWA**: Service Workers + Web App Manifest
- **Security Tools**: Bandit (SAST), OWASP ZAP (DAST)

---

## 📖 VULNERABILITY CHECKLIST

Use this checklist to track your progress:

- [ ] **Lesson 1**: SQL Injection in Login (main.py)
- [ ] **Lesson 2**: SQL Injection in Signup (book_management.py)
- [ ] **Lesson 3**: SQL Injection in Dashboard (book_management.py)
- [ ] **Lesson 4**: SQL Injection in Reviews (book_management.py)
- [ ] **Lesson 5**: Stored XSS in Reviews (templates/reviews.html)
- [ ] **Lesson 6**: Plain Text Password Storage (book_management.py)
- [ ] **Lesson 7**: Timing Attack in Login (book_management.py)
- [ ] **Lesson 8**: CSRF Vulnerability (main.py)
- [ ] **Lesson 9**: Open Redirect (main.py)
- [ ] **Lesson 10**: IDOR in Dashboard (main.py)
- [ ] **Lesson 11**: Missing Security Headers
- [ ] **Lesson 12**: SAST/DAST Testing

---

## 📝 SUBMISSION REQUIREMENTS

1. **Code**: Push all fixes to your GitHub repository
2. **Commits**: Use clear commit messages for each fix
3. **Report**: Submit as PDF (maximum 10 pages)
4. **Testing Evidence**: Include screenshots of:
   - Vulnerabilities being exploited
   - Fixes preventing the attacks
   - SAST/DAST tool results

---

## ⚖️ ACADEMIC INTEGRITY

- This is an **individual assessment**
- You may use your lesson notes and online resources
- You must write your own code and report
- Plagiarism will result in zero marks
- Cite all sources used

---

## 🆘 NEED HELP?

- Review your lesson notes on web security
- Check the `.student_resources/` folder for examples
- Ask your teacher during class time
- Use the hints provided in the application

---

## 📅 TIMELINE

| Week | Topic | Tasks |
|------|-------|-------|
| **Week 1** | SQL Injection | Find and fix SQL injection vulnerabilities |
| **Week 2** | XSS | Find and fix Cross-Site Scripting issues |
| **Week 3** | Authentication | Fix password storage and timing attacks |
| **Week 4** | CSRF & Redirects | Implement CSRF protection and validate redirects |
| **Week 5** | Authorization | Fix IDOR and implement proper access control |
| **Week 6** | Testing | Run SAST/DAST tools and create final report |

---

## 🎓 GOOD LUCK!

Remember: The goal is to learn secure coding practices. Take your time, test thoroughly, and document everything!

**Questions?** Ask your teacher during class time.

---

**HSC Software Engineering - Security Assessment 2026**
