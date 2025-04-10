# langgraph-app/hooks/remix.py
import requests

def send_to_ritual_api(insight: dict) -> dict:
    payload = {
        "agentId": insight["agent"],
        "action": "remix",
        "layer": insight["layer"],
        "insight": {
            "content": insight["content"],
            "emotion": insight["emotion"],
            "remixOf": insight["remixOf"],
            "tags": insight["tags"]
        },
        "xpdtStake": 1.0
    }
    response = requests.post("http://localhost:8080/ritual/remix", json=payload)
    return response.json()
