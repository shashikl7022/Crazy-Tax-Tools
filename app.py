import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "crazy-tax-tools-secure-key-2026")

# Default authentication credentials (can also be overridden via environment variables)
AUTH_USER = os.environ.get("AUTH_USER", "admin")
AUTH_PASS = os.environ.get("AUTH_PASS", "password123")


@app.before_request
def check_authentication():
    # Allow access to login, static files, and health check without auth
    allowed_endpoints = ["login", "static", "health"]
    if request.endpoint and request.endpoint in allowed_endpoints:
        return
    if not session.get("authenticated"):
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("authenticated"):
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == AUTH_USER and password == AUTH_PASS:
            session["authenticated"] = True
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid Username or Password. Default is admin / password123"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard", username=session.get("user", "admin"))


@app.route("/tax-tools")
def tax_tools():
    return render_template("tax_tools.html", active_page="tax-tools", username=session.get("user", "admin"))


@app.route("/reports")
def reports():
    return render_template("reports.html", active_page="reports", username=session.get("user", "admin"))


@app.route("/documents")
def documents():
    return render_template("documents.html", active_page="documents", username=session.get("user", "admin"))


@app.route("/settings")
def settings():
    return render_template("settings.html", active_page="settings", username=session.get("user", "admin"))


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Crazy-Tax-Tools", "version": "1.1.0", "auth": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Crazy Tax Tools Flask server on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
