from fastapi import FastAPI
import requests
import base64
import os

app = FastAPI()

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

DISPATCH_URL = "https://exit-interview-agent-1lo01a7d.livekit.cloud/agents/dispatch"

@app.post("/dispatch")
def dispatch_agent(payload: dict):
    auth = f"{LIVEKIT_API_KEY}:{LIVEKIT_API_SECRET}"
    encoded = base64.b64encode(auth.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/json",
    }

    r = requests.post(DISPATCH_URL, json=payload, headers=headers)
    return r.json()
