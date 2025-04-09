# langgraph-app/main.py

from langgraph.graph import StateGraph
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.critic import critic_agent
from hooks.mint import send_to_ritual_api as mint_hook
from hooks.remix import send_to_ritual_api as remix_hook
from hooks.validate import send_to_ritual_api as validate_hook

# Input quote for the demo
quote = "The truth is rarely pure and never simple."

# Create LangGraph pipeline
workflow = StateGraph()

# Step 1: Researcher Agent
research_output = researcher_agent(quote)
mint_response = mint_hook(research_output)
print("[Minted Insight]", mint_response)

# Step 2: Analyst Agent (Remix)
analysis_output = analyst_agent(research_output["content"])
analysis_output["remixOf"] = mint_response.get("insightId", "insight-001")  # Mock lineage
remix_response = remix_hook(analysis_output)
print("[Remixed Insight]", remix_response)

# Step 3: Critic Agent (Validation)
critique_output = critic_agent(analysis_output["content"])
critique_output["validatedId"] = remix_response.get("insightId", "insight-002")  # Mock lineage
validate_response = validate_hook(critique_output)
print("[Validated Insight]", validate_response)

print("\n>>> Demo complete. Ritual memory trail written to XpectraNet.")
