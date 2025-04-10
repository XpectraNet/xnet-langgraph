# main.py — XKO-aligned symbolic cognition loop
# Demonstrates a full L1 → L3 → L6 memory lifecycle using XpectraNet + LangGraph + ComposeDB
#
# ┌───────────────────────────────┐
# │      LangGraph Agent Loop     │
# └───────────────────────────────┘
# Researcher (L1): seed insight
#   → Analyst (L3): transform insight
#   → Critic (L6): validate
#   → Analyst (L3): remix again
#   → ... (loop until complete)
#
# Each step pushes symbolic memory to:
#   POST /insight/lifecycle
#     → Node.js Relay (ritual-to-compose)
#     → ComposeDB (Ceramic network)

# Load agent configuration with XKO and fallback support
from utils.load_agent_config import load_agent_config
AGENT_CONFIG = load_agent_config("config/agent-config.hybrid.json")

# Build symbolic workflow graph
def build_graph():
    # Initialize a new LangGraph pipeline
    builder = StateGraph()

    # Nodes represent memory lifecycle agents
    builder.add_node("research", researcher_agent)   # Mint: L1
    builder.add_node("analyze", analyst_agent)       # Remix: L3
    builder.add_node("critique", critic_agent)       # Validate: L6

    # Define memory evolution path
    builder.set_entry_point("research")
    builder.add_edge("research", "analyze")
    builder.add_edge("analyze", "critique")
    builder.add_edge("critique", "analyze")  # Loop for remixing deeper

    return builder.compile()

if __name__ == "__main__":
    print("🧠 Running XKO memory loop (L1 → L3 → L6)...\n")

    graph = build_graph()

    # Initialize shared memory state
    state = {
        "remix_depth": 0,
        "validated_count": 0,
        "trail": [],  # Stores insight lineage (ID trail)
        "agent_config": AGENT_CONFIG
    }

    MAX_DEPTH = 5
    MAX_VALIDATIONS = 3

    # Run symbolic loop
    while state["remix_depth"] < MAX_DEPTH and state["validated_count"] < MAX_VALIDATIONS:
        print(f"🔁 Cycle {state['remix_depth'] + 1} | Validated: {state['validated_count']}")
        state = graph.invoke(state)  # Trigger current agent

        if state.get("last_action") == "xko:validate":
            state["validated_count"] += 1

        state["remix_depth"] += 1

        # Track symbolic memory trail
        insight_id = state.get("insight_id") or state.get("final_id")
        if insight_id:
            state["trail"].append(insight_id)

        print(f"➡️ Insight ID: {insight_id}")
        print("")

    # Final trail summary
    print("✅ Loop complete. Final trail:")
    for i, node_id in enumerate(state["trail"], 1):
        print(f"  {i}. {node_id}")