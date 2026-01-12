from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import book_management as bm
import secrets
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)

# Home page - Login
@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    # VULNERABILITY: Open Redirect
    if request.method == "GET" and request.args.get("redirect"):
        redirect_url = request.args.get("redirect")
        return redirect(redirect_url)

    # Handle login
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # VULNERABILITY: SQL Injection in login + Timing Attack
        user = bm.checkLogin(username, password)

        if user:
            session['username'] = username
            session['member_id'] = user['member_id']
            return redirect("/dashboard.html")
        else:
            error = "Invalid username or password"
            return render_template("index.html", error=error)

    return render_template("index.html")


# Signup page
@app.route("/signup.html", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        # VULNERABILITY: SQL Injection in signup + Plain text passwords
        result = bm.insertMember(username, password, email)

        if result:
            success = "Account created successfully! Please login."
            return render_template("signup.html", success=success)
        else:
            error = "Username already exists"
            return render_template("signup.html", error=error)

    return render_template("signup.html")


# Dashboard - View borrowed books
@app.route("/dashboard.html", methods=["GET"])
def dashboard():
    if 'username' not in session:
        return redirect("/")

    # VULNERABILITY: Insecure Direct Object Reference (IDOR)
    member_id = request.args.get("id", session['member_id'])
    borrowed_books = bm.getBorrowedBooks(member_id)

    return render_template("dashboard.html",
                         username=session.get('username'),
                         borrowed_books=borrowed_books,
                         member_id=member_id)


# Book review submission
@app.route("/reviews.html", methods=["GET", "POST"])
def reviews():
    if 'username' not in session:
        return redirect("/")

    if request.method == "POST":
        book_title = request.form.get("book_title")
        review = request.form.get("review")

        # VULNERABILITY: SQL Injection + XSS
        bm.insertReview(session['member_id'], book_title, review)

        message = "Review submitted successfully!"
        return render_template("reviews.html", message=message)

    # VULNERABILITY: XSS in review display
    reviews_list = bm.getReviews()

    return render_template("reviews.html", reviews=reviews_list)


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
