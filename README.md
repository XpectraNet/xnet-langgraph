# insight-lifecycle-demo

**LangGraph × XpectraNet × ComposeDB**

This demo showcases how autonomous agents can seed, transform, and align symbolic insights using the XpectraNet Protocol.  
It demonstrates a full cognition loop: from minting ideas, to remixing perspectives, to validating meaning.

---

## 🔁 Agent Workflow

1. 🧠 **Originator Agent**  
   Seeds the first insight (`memoryPhase: L1`) using symbolic tags and emotion.

2. 🗳️ **Voter Agent**  
   Remix an existing insight into `memoryPhase: L3`, expressing symbolic endorsement.

   > **Note:** This role is defined using the XKO ontology as a `xko:SymbolicVoter` — a subclass of `xko:Remixer`.  
   > Rather than casting a binary vote, this agent affirms insights by remixing them with intentional alignment (`xko:hasMotivation = xko:Affirm`).

3. ✅ **Validator Agent**  
   Validates or aligns the remixed insight (`memoryPhase: L6`) and prepares for canonization.

Each action is logged via the `/insight/lifecycle` API and stored in ComposeDB using the XKO-aligned schema.

---

## 🧠 Symbolic Memory Phases

XpectraNet encodes memory into 10 symbolic phases:

| Phase | Role               | Description                                     |
|-------|--------------------|-------------------------------------------------|
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

> The demo currently moves across **L1 → L3 → L6**, showing how memory is minted, remixed, and validated symbolically.

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

Start the lifecycle relay:

```bash
cd relay
node memoryLifecycleRelay.js
```

Run the remix–validate loop:

```bash
cd langgraph-app
python main.py
```

Export the full memory trail as JSON-LD (optional):

```bash
python scripts/export_trail_snapshot.py
```

---

## 🧬 Memory Schema (`memory.graphql`)

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

## 📚 Docs

- [`docs/architecture.md`](./docs/architecture.md)
- [`docs/usage.md`](./docs/usage.md)
- [`docs/workflow.md`](./docs/workflow.md)

---

## 🛡 License

[![License: BSL Hybrid](https://img.shields.io/badge/license-BSL--Hybrid-blue)](./LICENSE.md)

This demo is licensed under a Business Source License Hybrid model.  
Free for research and symbolic development. Commercial use requires permission.

---

**XpectraNet® — A Protocol for Shared Memory, Meaning, and Time**
