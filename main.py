import os
import json
import base64
from flask import Flask, request, jsonify, abort
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv
from app.agents.scrum_master_agent import ScrumMasterAgent 

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
    
    interaction_type = data.get("type")

    # Handle Discord PING interaction (type 1)
    if interaction_type == 1: # PING
        return jsonify({"type": 1}) # PONG
    
    # Handle APPLICATION_COMMAND interaction (type 2)
    if interaction_type == 2:
        command_data = data.get("data", {})
        command_name = command_data.get("name")

        if command_name == "scrum":
            # Extract user input from the command options
            # Assuming the scrum command has an option named 'query' or 'input'
            user_input = ""
            options = command_data.get("options", [])
            if options:
                # This assumes the first option is the user's main input.
                # You might need to adjust this based on your command's actual option structure.
                # For example, if your option is named 'prompt':
                # user_input = next((opt['value'] for opt in options if opt['name'] == 'prompt'), "")
                user_input = options[0].get("value", "") 
                print(f"User input for scrum command: {user_input}")

            if not user_input:
                return jsonify({
                    "type": 4, 
                    "data": {"content": "You need to provide some input for the scrum master!"}
                })

            # Get response from ScrumMasterAgent
            try:
                response_text = ScrumMasterAgent.get_scrum_response_for_interaction(user_input)
                return jsonify({
                    "type": 4, 
                    "data": {"content": response_text}
                })
            except Exception as e:
                # Log the error for debugging
                print(f"Error processing /scrum command: {e}")
                return jsonify({
                    "type": 4, 
                    "data": {"content": "Sorry, I encountered an error trying to process your scrum request."}
                })

    # Fallback for other interaction types or unhandled commands
    return jsonify({"type": 4, "data": {"content": "Interaction received but not processed."}})

asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

if __name__ == "__main__":
    # Run the Flask app locally.
    app.run(debug=True)
