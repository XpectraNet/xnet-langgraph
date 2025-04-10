from hooks.validate import validate_insight

def critic_agent(state):
    print("🧠 CriticAgent is validating the insight...")

    result = validate_insight(
        agent_id="did:agent:critic-003",
        validated_id=state["insight_id"]
    )

    state["final_id"] = result.get("id")
    return state
