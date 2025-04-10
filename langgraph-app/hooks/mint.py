# langgraph-app/hooks/mint.py
import requests

RELAY_URL = "http://localhost:5000/insight/lifecycle"

def mint_insight(agent_id, content, emotion, tags, layer="L1"):
    payload = {
        "agentId": agent_id,
        "action": "mint",
        "layer": layer,
        "insight": {
            "content": content,
            "emotion": emotion,
            "tags": tags,
            "originType": "XInsight"
        },
        "xpdtStake": 1.0
    }
    response = requests.post(RELAY_URL, json=payload)
    return response.json()
