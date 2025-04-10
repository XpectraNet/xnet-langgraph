from hooks.remix import remix_insight
import random

def analyst_agent(state):
    config = state["agent_config"]["Analyst"]
    emotion = random.choice(config["xko:emotionProfile"])

    print("🔍 Analyst (L3) is remixing the insight...")

    remixed_content = f"Remixed: {state['content']} — reframed with symbolic context."

    response = remix_insight(
        agent_id=config["xko:agentId"],
        content=remixed_content,
        emotion=emotion,
        tags=config["xko:tags"],
        remix_of=state["insight_id"],
        layer=config["xko:memoryPhase"]
    )

    state["insight_id"] = response.get("id")
    state["content"] = remixed_content
    state["last_action"] = config["xko:action"]
    return state