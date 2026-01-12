import sqlite3
import os
import time

DATABASE = "database_files/library.db"

def init_db():
    """Initialize the database with tables and sample data"""
    if os.path.exists(DATABASE):
        return

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Create members table
    cur.execute('''
        CREATE TABLE members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT
        )
    ''')

    # Create books table
    cur.execute('''
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT,
            available INTEGER DEFAULT 1
        )
    ''')

    # Create borrowed_books table
    cur.execute('''
        CREATE TABLE borrowed_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            book_title TEXT,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id)
        )
    ''')

    # Create reviews table
    cur.execute('''
        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            book_title TEXT,
            review TEXT,
            date TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id)
        )
    ''')

    # Insert sample members (VULNERABILITY: Plain text passwords)
    cur.execute("INSERT INTO members (username, password, email) VALUES ('alice', 'password123', 'alice@library.com')")
    cur.execute("INSERT INTO members (username, password, email) VALUES ('bob', 'qwerty', 'bob@library.com')")
    cur.execute("INSERT INTO members (username, password, email) VALUES ('charlie', 'abc123', 'charlie@library.com')")

    # Insert sample books
    cur.execute("INSERT INTO books (title, author, isbn, available) VALUES ('Python Programming', 'John Smith', '978-1234567890', 1)")
    cur.execute("INSERT INTO books (title, author, isbn, available) VALUES ('Web Development', 'Jane Doe', '978-0987654321', 1)")
    cur.execute("INSERT INTO books (title, author, isbn, available) VALUES ('Database Design', 'Bob Johnson', '978-1122334455', 0)")

    # Insert sample borrowed books
    cur.execute("INSERT INTO borrowed_books (member_id, book_title, borrow_date, return_date) VALUES (1, 'Python Programming', '2026-01-01', '2026-01-15')")
    cur.execute("INSERT INTO borrowed_books (member_id, book_title, borrow_date, return_date) VALUES (1, 'Web Development', '2026-01-05', '2026-01-19')")
    cur.execute("INSERT INTO borrowed_books (member_id, book_title, borrow_date, return_date) VALUES (2, 'Database Design', '2026-01-10', '2026-01-24')")

    conn.commit()
    conn.close()


# VULNERABILITY: SQL Injection in login + Timing Attack
def checkLogin(username, password):
    """Check if login credentials are valid"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"SELECT * FROM members WHERE username = '{username}' AND password = '{password}'"

    # VULNERABILITY: Timing attack - different delays for valid/invalid users
    try:
        cur.execute(query)
        user = cur.fetchone()

        if user:
            time.sleep(0.5)  # Simulate processing time for valid user
        else:
            time.sleep(0.1)  # Faster response for invalid user

        conn.close()
        return user
    except:
        conn.close()
        return None


# VULNERABILITY: SQL Injection in member insertion
def insertMember(username, password, email):
    """Insert a new member"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    try:
        # VULNERABLE: Using f-string with user input + plain text password
        query = f"INSERT INTO members (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


# VULNERABILITY: SQL Injection in borrowed books lookup
def getBorrowedBooks(member_id):
    """Get borrowed books for a member"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    query = f"SELECT * FROM borrowed_books WHERE member_id = '{member_id}'"
    cur.execute(query)

    books = cur.fetchall()
    conn.close()

    return books


# VULNERABILITY: SQL Injection in review insertion
def insertReview(member_id, book_title, review):
    """Insert a book review"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # VULNERABLE: Using f-string with user input
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    query = f"INSERT INTO reviews (member_id, book_title, review, date) VALUES ('{member_id}', '{book_title}', '{review}', '{date}')"
    cur.execute(query)

    conn.commit()
    conn.close()


def getReviews():
    """Get all reviews"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT r.book_title, r.review, r.date, m.username FROM reviews r JOIN members m ON r.member_id = m.member_id ORDER BY r.date DESC")

    reviews = cur.fetchall()
    conn.close()

    return reviews


# Initialize database on import
init_db()
