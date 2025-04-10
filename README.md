
# Insight Lifecycle Demo

**LangGraph × XpectraNet × ComposeDB**

This demo showcases how autonomous agents can seed, transform, and align symbolic insights using the XpectraNet Protocol, which supports a persistent insight lifecycle and memory trail stored on ComposeDB.

---

## 🧠 What It Does

This is not just another LLM workflow.

It demonstrates a **full cognition loop**:

- LLM agents collaborate across memory phases
- Each insight becomes a verifiable memory node
- Trails are queryable by remix lineage, emotional state, or symbolic alignment

---

## 🔁 Symbolic Memory Phases

| Phase | Name       | Description                              |
|-------|------------|------------------------------------------|
| L1    | Seed       | A new insight is minted (origin thought) |
| L3    | Transform  | A remix or reframe of an existing idea   |
| L6    | Align      | The insight is validated or confirmed    |

Each phase is persisted using XpectraNet's lifecycle API and stored in ComposeDB.

---

## ⚙️ Stack Overview

| Layer         | Tool        | Purpose                              |
|---------------|-------------|--------------------------------------|
| Agent Logic   | LangGraph   | Multi-agent LLM orchestration        |
| Lifecycle API | XpectraNet  | Symbolic memory flow + staking logic |
| Storage       | ComposeDB   | Verifiable graph memory              |
| Identity      | Ceramic     | DID + signed insight authorship      |

---

## 🚀 Quickstart

```bash
# Clone the repo
git clone https://github.com/XpectraNet/insight-lifecycle-demo.git
cd insight-lifecycle-demo

# Start the relay
cd relay
npm install
node memoryLifecycleRelay.js
```

```bash
# In another terminal: run the agent pipeline
cd langgraph-app
pip install -r requirements.txt
python main.py
```

> Insights are pushed to: `http://localhost:5000/insight/lifecycle`

---

## 🧪 Query the Memory Trail

```graphql
query {
  insightIndex(first: 5) {
    edges {
      node {
        content
        memoryPhase
        remixOf
        validatedBy
        emotion
        tags
      }
    }
  }
}
```

Each node is signed, traceable, and queryable on ComposeDB.

---

## 📚 Documentation

- [`docs/architecture.md`](./docs/architecture.md) — System breakdown  
- [`docs/usage.md`](./docs/usage.md) — Setup & deployment  
- [`docs/graphql-queries.md`](./docs/graphql-queries.md) — Query examples  
- [`docs/workflow.md`](./docs/workflow.md) — Cognitive memory flow  

---

## ✅ Status

- [x] Working LangGraph flow (L1 → L3 → L6)
- [x] Insight trail stored on ComposeDB
- [x] Modular hook system (mint, remix, validate)
- [x] JSON-based lifecycle API
- [x] DID-linked authorship

---

## 💡 What's Next

- Canonization phase (L7)
- D3-based visual trail explorer
- XPDT staking rewards
- Multi-agent remix validation

---

## 🛡 License

[![License: XpectraNet Hybrid BSL](https://img.shields.io/badge/license-BSL--Hybrid-blue)](./LICENSE.md)

This repository is released under a Business Source License Hybrid model.  
It is open for research and remix, but requires permission for commercial use.  
See [LICENSE.md](./LICENSE.md) for full terms.

---

**XpectraNet® — A Protocol for Shared Memory, Meaning, and Time**

Built for memory. Anchored in thought. Powered by XPDT.
