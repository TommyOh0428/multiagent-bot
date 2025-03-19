import os
import json
import base64
from flask import Flask, request, jsonify, abort
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def verify_discord_signature(request):
    """
    Verifies the Discord signature from the incoming Flask request.
    Expects:
      - X-Signature-Ed25519 header
      - X-Signature-Timestamp header
      - The raw request body as sent by Discord.
    """
    PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    
    # Normalize header keys to lowercase to cover API Gateway cases
    headers = {k.lower(): v for k, v in request.headers.items()}
    signature = headers.get("x-signature-ed25519")
    timestamp = headers.get("x-signature-timestamp")
    
    if not signature and timestamp:
        abort(400, "missing signature")

    if signature and not timestamp:
        abort(400, "missing timestamp")

    if not signature and not timestamp:
        abort(400, "Missing signature and timestamp headers")
    
    # Get raw request body as text (ensuring no transformations occur)
    body = request.get_data(as_text=True)
    message = f"{timestamp}{body}".encode()
    
    try:
        verify_key.verify(message, bytes.fromhex(signature))
    except BadSignatureError:
        abort(401, "Bad Signature")

@app.route("/", methods=["POST"])
def interactions():
    # Verify the request signature strictly.
    verify_discord_signature(request)
    
    try:
        data = request.get_json()
    except Exception:
        abort(400, "Invalid JSON payload")
    
    # Handle Discord PING interaction (type 1)
    if data.get("type") == 1:
        return jsonify({"type": 1})
    
    # Process other interactions (e.g., slash commands) here.
    return jsonify({"type": 4, "data": {"content": "Interaction received!"}})

asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

if __name__ == "__main__":
    # Run the Flask app locally.
    app.run(debug=True)
