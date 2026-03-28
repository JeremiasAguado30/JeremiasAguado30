"""Aplicación Flask para Pescando (detector heurístico de phishing)."""

from __future__ import annotations

from flask import Flask, render_template, request

from analyzer import analyze_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    url_input = ""

    if request.method == "POST":
        url_input = request.form.get("url", "").strip()
        try:
            result = analyze_url(url_input)
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", result=result, error=error, url_input=url_input)


if __name__ == "__main__":
    # Debug True para desarrollo local; en producción usar WSGI + debug=False.
    app.run(host="0.0.0.0", port=5000, debug=True)
