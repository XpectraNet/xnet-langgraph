import requests
import random

RELAY_URL = "http://localhost:5000/insight/lifecycle"
EMOTIONS = ["Curiosity", "Wonder", "Observation"]

def researcher_agent(state):
    print("🔍 ResearcherAgent is thinking...")

    insight = {
        "content": "The origin of intelligence is symbolic pattern recognition.",
        "memoryPhase": "L1",
        "emotion": random.choice(EMOTIONS),
        "tags": ["origin", "pattern"]
    }

    res = requests.post(RELAY_URL, json=insight)
    insight_id = res.json().get("id", "unknown")

    print(f"✅ Researcher stored insight L1: {insight_id}")
    state["insight_id"] = insight_id
    state["content"] = insight["content"]
    return state
