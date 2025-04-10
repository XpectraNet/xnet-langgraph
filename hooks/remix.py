import requests
import datetime

def remix_insight(agent_id, content, emotion, tags, remix_of, layer):
    payload = {
        "@context": "https://xpectranet.org/xko#",
        "@type": "xko:Insight",
        "xko:agentId": agent_id,
        "xko:content": content,
        "xko:emotion": emotion,
        "xko:memoryPhase": layer,
        "xko:remixOf": remix_of,
        "xko:tags": tags,
        "xko:createdAt": datetime.datetime.utcnow().isoformat() + "Z"
    }

    try:
        res = requests.post("http://localhost:5000/insight/lifecycle", json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("❌ Remixing failed:", e)
        return {}