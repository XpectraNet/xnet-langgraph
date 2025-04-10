# langgraph-app/hooks/validate.py
import requests

def send_to_ritual_api(insight: dict) -> dict:
    payload = {
        "agentId": insight["agent"],
        "action": "validate",
        "layer": insight["layer"],
        "insight": {
            "validatedId": insight["validatedId"],
            "emotion": insight["emotion"]
        },
        "xpdtStake": 1.0
    }
    response = requests.post("http://localhost:8080/ritual/validate", json=payload)
    return response.json()
  
