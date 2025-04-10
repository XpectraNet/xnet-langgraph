from hooks.mint import mint_insight
import random

def researcher_agent(state):
    config = state["agent_config"]["Researcher"]
    emotion = random.choice(config["xko:emotionProfile"])

    print("🧠 Researcher (L1) is minting an insight...")

    response = mint_insight(
        agent_id=config["xko:agentId"],
        content="Curiosity often precedes clarity.",
        emotion=emotion,
        tags=config["xko:tags"],
        layer=config["xko:memoryPhase"]
    )

    state["insight_id"] = response.get("id")
    state["content"] = response.get("insight", {}).get("content")
    state["last_action"] = config["xko:action"]
    return state