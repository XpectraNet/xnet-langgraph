import requests

RELAY_URL = "http://localhost:5000/insight/lifecycle"

def validate_insight(agent_id, validated_id, emotion="Validation", layer="L6"):
    payload = {
        "agentId": agent_id,
        "action": "validate",
        "layer": layer,
        "insight": {
            "validatedId": validated_id,
            "emotion": emotion
        },
        "xpdtStake": 1.0
    }
    response = requests.post(RELAY_URL, json=payload)
    return response.json()
