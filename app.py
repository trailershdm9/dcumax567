from flask import Flask, render_template, request, jsonify, url_for
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

def transform_url(input_url: str) -> str:
    """Safe demo transform: keep path/query, replace host with current app host.
    This is just an example; replace with your real transformation logic.
    """
    try:
        parsed = urlparse(input_url)
        # If scheme is missing, assume https
        scheme = parsed.scheme or "https"
        # Keep the rest, host will be replaced by caller with request.host_url
        rebuilt = urlunparse((scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))
        return rebuilt
    except Exception:
        return input_url

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def api_convert():
    data = request.get_json(silent=True) or {}
    input_url = (data.get("url") or "").strip()
    if not input_url:
        return jsonify({ "ok": False, "error": "Missing 'url' in JSON body." }), 400

    transformed = transform_url(input_url)

    # Example: point to this app's base URL
    # Build a new URL on *this* host that contains the original link as a query param.
    current_base = request.url_root.rstrip('/')  # e.g., https://your-app.vercel.app
    current_path = url_for("download_proxy")  # '/dl'
    result_url = f"{current_base}{current_path}?src={transformed}"

    return jsonify({ "ok": True, "input": input_url, "result": result_url })

@app.route("/dl", methods=["GET"])
def download_proxy():
    # Placeholder endpoint to demonstrate "redirect or serve"
    # In a real app, you might validate & fetch a direct link here.
    src = request.args.get("src", "").strip()
    return (f"""
    <h1>Download Proxy</h1>
    <p>This is a demo endpoint. In production, you would validate and redirect or stream.</p>
    <p><strong>Source URL:</strong> {src}</p>
    <p><a href="/">Back</a></p>
    """), 200

# Vercel looks for 'app' at module import time.
# No need for app.run() here.
