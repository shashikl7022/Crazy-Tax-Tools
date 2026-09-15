from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/tax-tools")
def tax_tools():
    return render_template("tax_tools.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/documents")
def documents():
    return render_template("documents.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
