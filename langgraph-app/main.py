# main.py
# LangGraph workflow that emits symbolic memory to the insight lifecycle relay

from langgraph.graph import StateGraph, END
import requests
import random
import time

# Local relay URL
RELAY_URL = "http://localhost:5000/insight/lifecycle"

# Simulated emotions for symbolic context
EMOTIONS = ["Curiosity", "Tension", "Validation"]

# Simulate unique agent IDs (replace with DIDs in production)
AGENT_IDS = {
    "researcher": "did:agent:researcher-001",
    "analyst": "did:agent:analyst-002",
    "critic": "did:agent:critic-003"
}

# Agent 1: Researcher - Mints the initial insight
def researcher(state):
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

# Agent 2: Analyst - Transforms the insight
def analyst(state):
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

# Agent 3: Critic - Validates the transformed insight
def critic(state):
    print("🧠 CriticAgent is validating the insight...")
    insight = {
        "content": f"Aligned insight: {state['content']}",
        "memoryPhase": "L6",
        "emotion": "Validation",
        "validatedBy": [AGENT_IDS["critic"]],
        "remixOf": state["insight_id"],
        "tags": ["validated", "aligned"]
    }
    res = requests.post(RELAY_URL, json=insight)
    insight_id = res.json().get("id", "unknown")
    print(f"✅ Critic stored validation L6: {insight_id}")
    return {**state, "final_id": insight_id}


# Build the LangGraph state machine
builder = StateGraph()

# Register agents as nodes
builder.add_node("research", researcher)
builder.add_node("analyze", analyst)
builder.add_node("critique", critic)

# Define execution flow
builder.set_entry_point("research")
builder.add_edge("research", "analyze")
builder.add_edge("analyze", "critique")
builder.set_exit_point("critique")

# Compile and execute the graph
graph = builder.compile()

if __name__ == "__main__":
    print("🚀 Running LangGraph agentic memory cycle...")
    final_state = graph.invoke({})
    print("\n🌌 Final Symbolic Trail Completed:")
    print(final_state)
