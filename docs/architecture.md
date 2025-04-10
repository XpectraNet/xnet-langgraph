
# Insight Lifecycle Demo – Architecture Overview

This guide breaks down the architecture of the LangGraph × XpectraNet × ComposeDB system — a symbolic memory pipeline where LLM agents can co-author, remix, and validate insights with traceable semantic lineage.

---

## 🧠 Vision

To enable agentic systems to think together — not just by generating responses, but by contributing to a persistent, queryable, decentralized graph of symbolic memory.

---

## 📐 High-Level System Diagram

```
┌──────────────────┐     Insight Lifecycle API     ┌────────────────────────────┐
│ LangGraph Agents │ ────────────────────────────▶ │ Insight-to-Compose Relay   │
│   (LLMs)         │                              │      (Node.js)             │
└──────────────────┘                              └────────────────────────────┘
                                                         │
                                                         ▼
                                             ComposeDB + Ceramic Network
```

---

## 🧱 Stack Layers

| Layer         | Tool        | Role                                             |
|---------------|-------------|--------------------------------------------------|
| Agent Logic   | LangGraph   | LLM agent orchestration                          |
| Protocol      | XpectraNet  | Defines insight lifecycle, memory phases, trail  |
| Storage       | ComposeDB   | Stores symbolic memory as linked documents       |
| Identity      | Ceramic     | DID-backed identity and stream signing           |

---

## 🔁 Symbolic Flow: Seed → Transform → Align

### 1. `researcher_agent`
- Seeds an original thought (`memoryPhase: L1`)
- Hook: `mint_insight()`

### 2. `analyst_agent`
- Transforms insight (`memoryPhase: L3`)
- Hook: `remix_insight()` + `remixOf`

### 3. `critic_agent`
- Validates transformed thought (`memoryPhase: L6`)
- Hook: `validate_insight()` + `validatedBy`

Each step persists memory into ComposeDB via the relay.

---

## 🔗 Relay: `memoryLifecycleRelay.js`

- Lightweight Node.js API server
- Accepts POST `/insight/lifecycle`
- Transforms agent insight payloads into `createInsight` GraphQL mutations
- Uses `ComposeClient` to write to Ceramic Clay testnet

Example payload:

```json
{
  "agentId": "did:agent:001",
  "action": "remix",
  "layer": "L3",
  "insight": {
    "content": "Remixed idea",
    "emotion": "Tension",
    "tags": ["reframe", "symbolic"],
    "remixOf": "did:ceramic:abc123"
  },
  "xpdtStake": 1.0
}
```

---

## 🧬 ComposeDB Schema

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

Query insights by trail, emotion, validation, phase, or timestamp.

---

## 🛠 Developer Notes

- Agents use `StateGraph` to define ordered symbolic logic
- Hooks modularize lifecycle API calls (mint/remix/validate)
- ComposeDB allows full-text insight graph queries with traceable lineage

---

## ✅ Benefits

- Verifiable symbolic cognition
- Multi-agent insight evolution
- Queryable memory trails
- Open composability (D3.js, XPDT staking, Circle consensus)

---

## 📌 Next Enhancements

- Canonization and archival (L7, L8)
- XPDT-powered incentive layers
- Validator circles and remix scoring
- Insight trail visualizer (D3)

---

**XpectraNet® — Insight Lifecycle Protocol for Symbolic Agents**

Built for memory. Anchored in thought. Powered by XPDT.
