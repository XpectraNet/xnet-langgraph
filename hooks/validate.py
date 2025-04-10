import requests
import datetime

def validate_insight(agent_id, validated_id, emotion, tags, layer):
    payload = {
        "@context": "https://xpectranet.org/xko#",
        "@type": "xko:Insight",
        "xko:agentId": agent_id,
        "xko:memoryPhase": layer,
        "xko:emotion": emotion,
        "xko:validatedBy": [agent_id],
        "xko:tags": tags,
        "xko:remixOf": validated_id,
        "xko:createdAt": datetime.datetime.utcnow().isoformat() + "Z"
    }

    try:
        res = requests.post("http://localhost:5000/insight/lifecycle", json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("❌ Validation failed:", e)
        return {}