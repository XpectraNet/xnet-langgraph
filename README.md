
# Insight Lifecycle Demo

**LangGraph × XpectraNet × ComposeDB**

This demo showcases how autonomous agents can mint, transform, align, and resolve symbolic insights using the XpectraNet Protocol — with persistent graph memory stored on ComposeDB and identity secured via Ceramic.

It demonstrates a full-stack cognition flow:

- **LangGraph** orchestrates agent steps (LLM-driven reasoning)
- **XpectraNet** defines symbolic memory phases and lineage
- **ComposeDB** stores insights as verifiable documents
- **Ceramic** provides decentralized identity + signing

---

## 🔁 Memory Flow (Seed → Transform → Align)

```
Researcher Agent → Analyst Agent → Critic Agent
   (L1 Insight) → (L3 Remix) → (L6 Validation)
```

Each phase is recorded and queryable — creating an evolving trail of **cognitive lineage**.

---

## 🌐 Stack Summary

| Layer         | Tool        | Purpose                              |
|---------------|-------------|--------------------------------------|
| Agent Logic   | LangGraph   | Multi-agent LLM orchestration        |
| Memory Engine | XpectraNet  | Insight lifecycle & symbolic protocol|
| Storage       | ComposeDB   | Verifiable graph memory              |
| Identity      | Ceramic     | DID + signed insight actions         |

---

## 🔧 Deploy ComposeDB model (first time only):
```bash
composedb composite:compile memory.graphql > model.json
composedb composite:deploy model.json
```
---

## 🚀 Quickstart: Try It in Minutes
```bash
# 1. Clone the demo:
git clone https://github.com/XpectraNet/insight-lifecycle-demo.git
cd insight-lifecycle-demo

# 2. Start the symbolic relay (Node.js):
cd relay
npm install
node memoryLifecycleRelay.js
```
🔌 Starts the Insight Lifecycle API at http://localhost:5000/insight/lifecycle

---

## 🤖 Run the Agentic Memory Flow:
In another terminal:
```bash
cd langgraph-app
pip install -r requirements.txt
python main.py
```

🧠 This triggers:

- Agent 1: Seeds an insight (memoryPhase: L1)
- Agent 2: Transforms the thought (L3)
- Agent 3: Aligns it with symbolic weight (L6)

Each step is stored in ComposeDB — creating a verifiable insight trail.

---

## 🔍 Explore Insight Graph
Query your agent memory trail via GraphQL:
```graphql
query {
  insightIndex(first: 5, filters: {memoryPhase: "L3"}) {
    edges {
      node {
        content
        memoryPhase
        emotion
        remixOf
        validatedBy
        tags
      }
    }
  }
}
```
💡 Powered by Ceramic — every memory is signed, persisted, and composable.

---

## 🧠 What Just Happened?
You just ran a 3-agent cognitive pipeline that:

- Created symbolic insight
- Remixed it with emotion + lineage
- Validated the memory
- Persisted everything on a decentralized graph

This is semantic memory for agents.
This is XpectraNet.

---

## 📖 Docs

- [`docs/architecture.md`](./docs/architecture.md) – Full system breakdown  
- [`docs/usage.md`](./docs/usage.md) – Deployment + testing guide  
- [`docs/graphql-queries.md`](./docs/graphql-queries.md) – Querying the insight graph  

---

**XpectraNet® — Insight Lifecycle Protocol for Agentic Collaboration**  
Built for agents. Anchored in thought. Powered by XPDT.
