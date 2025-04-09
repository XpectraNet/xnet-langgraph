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
