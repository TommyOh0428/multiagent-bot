import json

import pytest
from fastapi import HTTPException
from nacl.signing import SigningKey

from main import verify_discord_signature


def test_verify_discord_signature(monkeypatch):
    signing_key = SigningKey.generate()
    body = json.dumps({"type": 1}).encode()
    timestamp = "1234567890"
    signature = signing_key.sign(timestamp.encode() + body).signature.hex()
    monkeypatch.setenv("DISCORD_PUBLIC_KEY", signing_key.verify_key.encode().hex())

    verify_discord_signature(signature, timestamp, body)


def test_verify_discord_signature_rejects_invalid_signature(monkeypatch):
    signing_key = SigningKey.generate()
    monkeypatch.setenv("DISCORD_PUBLIC_KEY", signing_key.verify_key.encode().hex())

    with pytest.raises(HTTPException) as exc_info:
        verify_discord_signature("00" * 64, "1234567890", b'{"type": 1}')

    assert exc_info.value.status_code == 401
