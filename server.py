from flask import Flask, render_template, request, redirect, session, url_for

# -----------------------------------------------------
# Imports
# -----------------------------------------------------
from flask import Flask, render_template, request, redirect, session, url_for
from flask_mail import Mail, Message

# -----------------------------------------------------
# Flask App Setup
# -----------------------------------------------------
app = Flask(__name__)
app.secret_key = "campusaid_secret_key"  # needed for session handling

# Temporary in-memory storage for demo
users = {
    "teacher": {"password": "teacher123", "role": "teacher"},
}

# -----------------------------------------------------
# ROUTES
# -----------------------------------------------------

# Home page (public)
@app.route("/")
def home():
    return render_template("index.html")

# Lost & Found
@app.route("/lost_found")
def lost_found():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("lostfound.html", user=session.get("user"))


# Ask a Senior
@app.route("/ask_senior")
def ask_senior():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("ask_senior.html", user=session.get("user"))


# Peer Tutoring
@app.route("/peer_tutoring")
def peer_tutoring():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("peer_tutoring.html", user=session.get("user"))

# -----------------------------------------------------
# AUTHENTICATION
# -----------------------------------------------------

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_input = request.form.get("username")  # user can type email or username
        password = request.form.get("password")

        # loop through all saved users
        for username, info in users.items():
            if login_input == username or login_input == info.get("email"):
                if password == info["password"]:
                    session["user"] = username
                    session["role"] = info["role"]
                    return redirect(url_for("home"))
                else:
                    return render_template("login.html", error="Incorrect password")
        return render_template("login.html", error="User not found")

    return render_template("login.html")


# Sign-up
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if username not in users:
            users[username] = {
                "email": email,
                "password": password,
                "role": "student"
            }
            session["user"] = username
            session["role"] = "student"
            return redirect(url_for("home"))
        else:
            return render_template("signin.html", error="Username already exists")

    return render_template("signin.html")


# Teacher dashboard (login required + must be teacher)
@app.route("/teacher_dashboard")
def teacher_dashboard():
    if "user" not in session or session.get("role") != "teacher":
        return redirect(url_for("login"))
    return render_template("teachers_dashboard.html")


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -----------------------------------------------------
# MAIN ENTRY
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
