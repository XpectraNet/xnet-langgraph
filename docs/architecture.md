# LangGraph × XpectraNet × ComposeDB: Architecture Overview

## Vision

Enable LangGraph agents to generate persistent, symbolic memory using the XpectraNet Protocol — where every thought is seeded, transformed, aligned, and resolved into a decentralized graph memory structure powered by ComposeDB.

---

## System Overview

```
┌──────────────────┐     Insight Lifecycle API    ┌────────────────────────────┐
│ LangGraph Agents │ ───────────────────────────▶ │ Insight-to-Compose Relay   │
│   (LLMs)         │                              │      (Node.js)             │
└──────────────────┘                              └────────────────────────────┘
                                                         │
                                                         ▼
                                             ComposeDB + Ceramic Network
```

---

## Architecture Breakdown

### LangGraph Agents (Python)
- Use LLMs to perform reasoning steps.
- Each step emits a symbolic action:
  - `seed`, `transform`, `align`
- Sends output to the `/insight/lifecycle` endpoint of the Node relay.

**Dependencies:**
```bash
pip install langgraph openai langchain requests
```

### Insight-to-Compose Relay (Node.js)
- Accepts JSON payloads from agents.
- Maps symbolic structure to ComposeDB GraphQL mutation.
- Connects to Ceramic network (Clay testnet).

**Dependencies:**
```bash
npm install express @ceramicnetwork/http-client graphql-request
```

### ComposeDB (GraphQL + Ceramic)
- Stores symbolic insights with remix lineage.
- Each record is signed with a DID (agent identity).
- Schema-defined insight structure:
```graphql
type Insight @createModel(accountRelation: LIST) {
  content: String!
  memoryPhase: String!
  emotion: String
  remixOf: DID
  validatedBy: [DID]
  tags: [String]
  createdAt: DateTime!
}
```

**To deploy:**
```bash
composedb composite:compile memory.graphql > model.json
composedb composite:deploy model.json
```

---

## Flow Summary

1. `ResearcherAgent` seeds a Phase 1 insight.
2. `AnalystAgent` transforms it into Phase 3.
3. `CriticAgent` aligns the insight as Phase 6.
4. All symbolic states are written to ComposeDB as cognitive lineage.

---

## STEP-BY-STEP DEEP DIVE

### 1. LangGraph (Agentic Cognition)
- Why: Orchestrates multiple LLM agents in a structured sequence.
- What Happens: Each agent runs a reasoning step and produces an insight.
- Under the Hood: LangGraph uses a directed state graph; nodes are async functions.
- Why It’s Widely Adopted: It’s the standard for multi-agent workflows in LangChain/OpenAI ecosystems.

### 2. Insight Lifecycle Relay (Symbolic Bridge)
- Why: Converts symbolic agent output into structured memory.
- What Happens: LangGraph POSTs JSON to `/insight/lifecycle`. The relay formats + forwards to ComposeDB.
- Under the Hood: It parses payloads, maps fields (e.g., `remixOf`, `validatedBy`) and signs data.
- Why It’s Widely Adopted: Node.js relays are ideal for connecting LLM logic to decentralized storage layers.

### 3. ComposeDB (Decentralized Memory Graph)
- Why: Stores verifiable symbolic memory with full lineage + identity.
- What Happens: Insights are stored as documents with `@createModel`. You can query or traverse trails.
- Under the Hood: Ceramic streams track version history; ComposeDB gives a GraphQL API.
- Why It’s Widely Adopted: Projects like Lens, Gitcoin, and FWB use ComposeDB for user-owned, queryable memory.

### 4. Querying the Graph (Cognitive Lineage)
- Why: Allows explorers, validators, or agents to traverse cognition history.
- What Happens: You query insights by `memoryPhase`, `remixOf`, `tags`, or emotional alignment.
- Under the Hood: It’s GraphQL — composable, filterable, and extendable.
- Why It’s Widely Adopted: Ecosystem tools like Tableland, Lit, and IDX work seamlessly with this structure.

---

## Why This Stack Works

| Layer         | Tool        | Purpose                              | Used By                        |
|---------------|-------------|--------------------------------------|--------------------------------|
| Agent Logic   | LangGraph   | Multi-agent LLM orchestration        | LangChain, Microsoft, OpenAI   |
| Insight Lifecycle | XpectraNet  | Symbolic cognition protocol              | You (foundationally unique)    |
| Storage       | ComposeDB   | Verifiable graph memory              | Gitcoin, Lens, FWB             |
| Identity      | Ceramic     | DID + signed insight actions         | Decentralized infra projects   |

---

## Next Steps

- [ ] Add resolve (canonization) and close (archival) phases.
- [ ] Visualize insight lineage via D3.
- [ ] Enable XPDT staking + Circle consensus.
- [ ] Host relay publicly for live trails.

---

**XpectraNet® — Insight Lifecycle Protocol for Agentic Collaboration**

Built for agents. Anchored in thought. Powered by XPDT.
