# insight-lifecycle-demo

**LangGraph × XpectraNet × ComposeDB (XKO-aligned)**

This demo shows how agents co-evolve symbolic memory across three key phases:
- Mint → Remix → Validate (L1 → L3 → L6)
- Each insight is stored using the Xpectra Knowledge Ontology (XKO)
- All memory is routed through a Node.js relay to ComposeDB

---

## 🔁 Agent Workflow (L1 → L3 → L6)

| Agent     | Phase | Role        | Action               |
|-----------|--------|-------------|-----------------------|
| Researcher | L1     | Originator  | Seeds original insight (`mint_insight`)  
| Analyst    | L3     | Remixer     | Transforms content with lineage (`remix_insight`)  
| Critic     | L6     | Validator   | Aligns memory with meaning (`validate_insight`)  

Each symbolic act is a valid `xko:Insight` and recorded as a node in the ComposeDB graph.

---

## ⚙️ How It Works

- **LangGraph** runs a loop: Researcher → Analyst → Critic → Analyst...  
- **Each step posts to `/insight/lifecycle`** on the local relay  
- **Relay normalizes `xko:` fields and submits to ComposeDB**  
- **GraphQL insight nodes** are persisted with `memoryPhase`, `remixOf`, `validatedBy`, `tags`, and more

---

## 🧠 Symbolic Memory Phases (XKO)

| Phase | Symbolic Role      | Description                                    |
|-------|--------------------|------------------------------------------------|
| L0    | Perception         | Raw input or sensed change                     |
| L1    | Mint               | New insight is created                         |
| L2    | Reflection         | Internal resonance or feedback                 |
| L3    | Remix              | Insight is transformed or re-framed            |
| L4    | Divergence         | Branches into alternative symbolic paths       |
| L5    | Resonance          | Shared symbolic attraction emerges             |
| L6    | Validation         | Insight is aligned with meaning                |
| L7    | Canonization       | Consensus reached through Circle quorum        |
| L8    | Archival           | Insight preserved for long-term reference      |
| L9    | Mythic Integration | Transcends context, becomes symbolic myth      |

> This demo walks from L1 → L3 → L6 and loops to L3, simulating symbolic refinement.

---

## 📦 Stack Overview

| Layer         | Tool        | Purpose                              |
|---------------|-------------|--------------------------------------|
| Agent Logic   | LangGraph   | Multi-agent LLM orchestration        |
| Lifecycle API | XpectraNet  | Symbolic memory flow + staking logic |
| Storage       | ComposeDB   | Verifiable memory graph              |
| Identity      | Ceramic     | DID + signed authorship              |

---

## 🚀 Run the Demo

Start the lifecycle relay server:

```bash
cd relay
node memoryLifecycleRelay.js
```

Run the agent loop:

```bash
cd langgraph-app
python main.py
```

Export full symbolic trail (optional):

```bash
python scripts/export_trail_snapshot.py
```

---

## 🛠 Project Structure

```
insight-lifecycle-demo/
├── config/                  # agent-config.xko.json
├── agents/                  # Researcher, Analyst, Critic
├── hooks/                   # mint, remix, validate
├── relay/compose/           # memory.graphql + model-definition.js
├── relay/memoryLifecycleRelay.js
├── main.py                  # LangGraph loop entry
```

---

## 🧬 Schema Overview

```graphql
type Insight @createModel(accountRelation: LIST, description: "xko:Insight") {
  content: String!
  memoryPhase: String!
  emotion: String
  remixOf: DID
  validatedBy: [DID]
  tags: [String]
  createdAt: DateTime!
}
```

---

## 🛡 License

[![License: BSL Hybrid](https://img.shields.io/badge/license-BSL--Hybrid-blue)](./LICENSE.md)

Open for research, remix, and symbolic experimentation.  
Commercial use requires explicit permission.

---

**XpectraNet® — The Memory Protocol for Collaborative AI Cognition**
