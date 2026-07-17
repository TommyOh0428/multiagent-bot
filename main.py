import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool
from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from agents.scrum_master_agent import ScrumMasterAgent


load_dotenv()

app = FastAPI(title="Multiagent Discord Bot")


def verify_discord_signature(
    signature: str | None, timestamp: str | None, body: bytes
) -> None:
    """Verify that an HTTP interaction was signed by Discord."""
    public_key = os.getenv("DISCORD_PUBLIC_KEY") or os.getenv("PUBLIC_KEY")
    if not public_key:
        raise HTTPException(
            status_code=500, detail="Discord public key is not configured"
        )
    if not signature or not timestamp:
        raise HTTPException(status_code=401, detail="Missing Discord signature headers")

    try:
        verify_key = VerifyKey(bytes.fromhex(public_key))
        verify_key.verify(timestamp.encode() + body, bytes.fromhex(signature))
    except (ValueError, BadSignatureError) as exc:
        raise HTTPException(
            status_code=401, detail="Invalid Discord signature"
        ) from exc


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/")
async def interactions(request: Request) -> dict:
    body = await request.body()
    verify_discord_signature(
        request.headers.get("x-signature-ed25519"),
        request.headers.get("x-signature-timestamp"),
        body,
    )

    try:
        data = json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise HTTPException(status_code=400, detail="Invalid JSON payload") from exc

    interaction_type = data.get("type")
    if interaction_type == 1:
        return {"type": 1}

    if interaction_type == 2:
        command_data = data.get("data", {})
        if command_data.get("name") == "scrum":
            options = command_data.get("options", [])
            user_input = options[0].get("value", "") if options else ""
            if not user_input:
                return {
                    "type": 4,
                    "data": {
                        "content": "You need to provide some input for the scrum master!"
                    },
                }

            try:
                response_text = await run_in_threadpool(
                    ScrumMasterAgent.get_scrum_response_for_interaction,
                    user_input,
                )
            except Exception as exc:
                # Avoid exposing provider or credential errors to Discord users.
                print(f"Error processing /scrum command: {exc}")
                return {
                    "type": 4,
                    "data": {
                        "content": "Sorry, I encountered an error trying to process your scrum request."
                    },
                }

            return {"type": 4, "data": {"content": response_text}}

    return {
        "type": 4,
        "data": {"content": "Interaction received but not processed."},
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
