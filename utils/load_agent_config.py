import json

def load_agent_config(path="config/agent-config.hybrid.json"):
    """
    Loads agent config and resolves both plain and XKO-aligned field names.
    Returns a dictionary indexed by role name.
    """
    with open(path) as f:
        config = json.load(f)

    agents = {}
    for agent in config.get("agents", []):
        role = agent.get("xko:role") or agent.get("role")
        agents[role] = {
            "agentId": agent.get("xko:agentId") or agent.get("agentId"),
            "action": agent.get("xko:action") or agent.get("action"),
            "memoryPhase": agent.get("xko:memoryPhase") or agent.get("memoryPhase"),
            "emotionProfile": agent.get("xko:emotionProfile") or agent.get("emotionProfile"),
            "tags": agent.get("xko:tags") or agent.get("tags"),
            "type": agent.get("@type") or "Agent",
            "context": config.get("@context", "https://xpectranet.org/xko#")
        }
    return agents