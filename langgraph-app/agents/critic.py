import requests

RELAY_URL = "http://localhost:5000/insight/lifecycle"
CRITIC_DID = "did:agent:critic-003"

def critic_agent(state):
    print("🧠 CriticAgent is validating the insight...")

    insight = {
        "content": f"Aligned insight: {state['content']}",
        "memoryPhase": "L6",
        "emotion": "Validation",
        "validatedBy": [CRITIC_DID],
        "remixOf": state["insight_id"],
        "tags": ["validated", "aligned"]
    }

    res = requests.post(RELAY_URL, json=insight)
    insight_id = res.json().get("id", "unknown")

    print(f"✅ Critic stored validation L6: {insight_id}")
    return {**state, "final_id": insight_id}
