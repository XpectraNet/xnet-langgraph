# main.py — LangGraph Insight Lifecycle Demo
# Executes a 3-agent flow where each step generates symbolic memory
# and persists it to ComposeDB via the XpectraNet lifecycle protocol

from langgraph.graph import StateGraph
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.critic import critic_agent

# ┌─────────────────────┐
# │ LangGraph Agent Flow│
# └─────────────────────┘
# Researcher: seed insight → Analyst: transform insight → Critic: validate
#
# Each step pushes symbolic memory to:
#    POST /insight/lifecycle (Node.js Relay → ComposeDB)

# Initialize a new LangGraph pipeline
builder = StateGraph()

# Register each symbolic agent node
builder.add_node("research", researcher_agent)   # L1 - Seed
builder.add_node("analyze", analyst_agent)       # L3 - Transform
builder.add_node("critique", critic_agent)       # L6 - Validate

# Define the execution flow
builder.set_entry_point("research")
builder.add_edge("research", "analyze")
builder.add_edge("analyze", "critique")
builder.set_exit_point("critique")

# Compile the executable graph
graph = builder.compile()

if __name__ == "__main__":
    print("🚀 Starting symbolic cognition flow...")
    
    # Pass in empty memory state for LangGraph to update
    final_state = graph.invoke({})

    print("\n🧠 Symbolic Memory Lifecycle Completed:")
    print(f"Final Insight ID: {final_state.get('final_id')}")
