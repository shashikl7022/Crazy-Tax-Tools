import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard")


@app.route("/tax-tools")
def tax_tools():
    return render_template("tax_tools.html", active_page="tax-tools")


@app.route("/reports")
def reports():
    return render_template("reports.html", active_page="reports")


@app.route("/documents")
def documents():
    return render_template("documents.html", active_page="documents")


@app.route("/settings")
def settings():
    return render_template("settings.html", active_page="settings")


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Crazy-Tax-Tools", "version": "1.0.0"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
