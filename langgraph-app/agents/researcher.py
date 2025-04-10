from hooks.mint import mint_insight
import random

def researcher_agent(state):
    print("🔍 ResearcherAgent is thinking...")

    content = "The origin of intelligence is symbolic pattern recognition."
    emotion = random.choice(["Curiosity", "Inspiration"])
    tags = ["seed", "symbolic"]

    result = mint_insight(
        agent_id="did:agent:researcher-001",
        content=content,
        emotion=emotion,
        tags=tags
    )

    state["insight_id"] = result.get("id")
    state["content"] = content
    return state
