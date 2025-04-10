import requests
import datetime

def mint_insight(agent_id, content, emotion, tags, layer):
    payload = {
        "@context": "https://xpectranet.org/xko#",
        "@type": "xko:Insight",
        "xko:agentId": agent_id,
        "xko:content": content,
        "xko:emotion": emotion,
        "xko:memoryPhase": layer,
        "xko:tags": tags,
        "xko:createdAt": datetime.datetime.utcnow().isoformat() + "Z"
    }

    try:
        res = requests.post("http://localhost:5000/insight/lifecycle", json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("❌ Minting failed:", e)
        return {}