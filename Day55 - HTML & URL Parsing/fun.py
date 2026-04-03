from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

users = {
    "admin": "1234"
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["user"] = username
            return f"Logged in as {username}"
        return "Invalid credentials"

    return """
        <form method="post">
            <input name="username" placeholder="username">
            <input name="password" placeholder="password" type="password">
            <button type="submit">Login</button>
        </form>
    """

def login_required(function):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return function(*args, **kwargs)
        return redirect(url_for("login"))
    return wrapper

@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {session['user']} to your dashboard"

@app.route("/logout")
def logout():
    session.pop("user", None)
    return "Logged out"

if __name__ == "__main__":
    app.run(debug=True)