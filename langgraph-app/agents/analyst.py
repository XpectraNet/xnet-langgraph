from hooks.remix import remix_insight
import random

def analyst_agent(state):
    print("📘 AnalystAgent is remixing the insight...")

    content = f"Building on: {state['content']} — this suggests cognition emerges through structure."
    emotion = random.choice(["Tension", "Depth", "Expansion"])
    tags = ["structure", "cognition"]

    result = remix_insight(
        agent_id="did:agent:analyst-002",
        content=content,
        emotion=emotion,
        tags=tags,
        remix_of=state["insight_id"]
    )

    state["insight_id"] = result.get("id")
    state["content"] = content
    return state
