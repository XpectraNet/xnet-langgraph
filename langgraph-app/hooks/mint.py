# langgraph-app/hooks/mint.py
import requests

def send_to_ritual_api(insight: dict) -> dict:
    payload = {
        "agentId": insight["agent"],
        "action": "mint",
        "layer": insight["layer"],
        "insight": {
            "content": insight["content"],
            "emotion": insight["emotion"],
            "tags": insight["tags"],
            "originType": "XInsight"
        },
        "xpdtStake": 1.0
    }
    response = requests.post("http://localhost:8080/ritual/mint", json=payload)
    return response.json()
