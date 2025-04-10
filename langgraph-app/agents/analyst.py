import requests
import random

RELAY_URL = "http://localhost:5000/insight/lifecycle"
EMOTIONS = ["Tension", "Skepticism", "Structure"]

def analyst_agent(state):
    print("📘 AnalystAgent is remixing the insight...")

    insight = {
        "content": f"Building on: {state['content']} — this suggests cognition emerges through structure.",
        "memoryPhase": "L3",
        "emotion": random.choice(EMOTIONS),
        "remixOf": state["insight_id"],
        "tags": ["structure", "cognition"]
    }

    res = requests.post(RELAY_URL, json=insight)
    insight_id = res.json().get("id", "unknown")

    print(f"✅ Analyst stored remix L3: {insight_id}")
    state["insight_id"] = insight_id
    state["content"] = insight["content"]
    return state
