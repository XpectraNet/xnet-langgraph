# LangGraph × XpectraNet Demo

**Repository:** `XpectraNet/xnet-langgraph`  
**Package Base:** `org.xpectranet.demo.langgraph`

---

## Overview

This demo showcases how LangGraph agents can mint, remix, validate, and canonize symbolic insights using the XpectraNet Protocol — enabling collaborative memory, semantic lineage, and trusted cognition.

XpectraNet is the first symbolic memory protocol for collaborative AI. This integration gives LangGraph agents access to persistent ritual memory across layers, with XPDT staking, emotional traceability, and remix logic.

---

## Demo Use Case

> **Was the Quote True?**

Three LangGraph agents collaborate:
- `ResearcherAgent`: Gathers context from an LLM
- `AnalystAgent`: Summarizes implications
- `CriticAgent`: Validates or challenges the interpretation

Each step triggers a symbolic memory action on XpectraNet:
- **Mint**: First insight (L0–L1)
- **Remix**: Structural divergence (L3–L5)
- **Validate**: Emotional resonance (L6)
- **Canonize**: Consensus insight (L7)

---

## Folder Structure

```
xnet-langgraph/
├── README.md
├── langgraph-app/
│   ├── main.py                  # LangGraph orchestration logic
│   ├── agents/
│   │   ├── researcher.py
│   │   ├── analyst.py
│   │   └── critic.py
│   └── hooks/
│       ├── mint.py              # Calls POST /ritual/mint
│       ├── remix.py             # Calls POST /ritual/remix
│       └── validate.py
├── xpectranet-adapter/
│   ├── pom.xml                  # Spring Boot Java app
│   └── src/main/java/org/xpectranet/demo/langgraph/
│       └── XpectraNetLangGraphAdapter.java
├── .env.example
└── LICENSE
```

---

## Integration Flow

1. Agents perform LLM tasks via LangGraph
2. Hooks trigger HTTP calls to `XpectraNetLangGraphAdapter`
3. Adapter connects to XpectraNet's `/ritual/perform` API
4. XPDT is staked, remix lineage is recorded, memory trail evolves

---

## Getting Started

### 1. Clone Repo
```bash
git clone https://github.com/XpectraNet/xnet-langgraph.git
```

### 2. Launch Java Adapter
```bash
cd xpectranet-adapter
./mvnw spring-boot:run
```

### 3. Run Demo Agents
```bash
cd langgraph-app
python main.py
```

---

## License

- Java adapter licensed under BSL Hybrid 1.1 (Business Source License)
- Demo agents licensed under MIT for open remix and experimentation

---

## Learn More

- https://xpectra.net/codex
- https://github.com/XpectraNet/x0-agent
- https://www.langchain.com/langgraph

**XpectraNet® — Symbolic Memory for Agentic Cognition**
