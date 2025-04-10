from hooks.validate import validate_insight
import random

def critic_agent(state):
    config = state["agent_config"]["Critic"]
    emotion = random.choice(config["xko:emotionProfile"])

    print("✅ Critic (L6) is validating the remix...")

    response = validate_insight(
        agent_id=config["xko:agentId"],
        validated_id=state["insight_id"],
        emotion=emotion,
        tags=config["xko:tags"],
        layer=config["xko:memoryPhase"]
    )

    state["final_id"] = response.get("id")
    state["last_action"] = config["xko:action"]
    return state