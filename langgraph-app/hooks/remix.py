import requests

RELAY_URL = "http://localhost:5000/insight/lifecycle"

def remix_insight(agent_id, content, emotion, tags, remix_of, layer="L3"):
    payload = {
        "agentId": agent_id,
        "action": "remix",
        "layer": layer,
        "insight": {
            "content": content,
            "emotion": emotion,
            "tags": tags,
            "remixOf": remix_of
        },
        "xpdtStake": 1.0
    }
    response = requests.post(RELAY_URL, json=payload)
    return response.json()
