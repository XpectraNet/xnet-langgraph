# LangGraph × XpectraNet × ComposeDB: Architecture Overview

## Vision

Enable autonomous agents to mint, remix, and validate symbolic memory using the XpectraNet protocol —  
recording each step in a decentralized graph (ComposeDB) with structure grounded in the Xpectra Knowledge Ontology (XKO).

---

## System Overview

```
┌───────────────────────────────┐    /insight/lifecycle     ┌─────────────────────────────┐
│ LangGraph Agent Loop.         │ ────────────────────────▶ │ Node.js Relay (Ritual Proxy)│
│ (Research → Remix → Validate) │                           └─────────────────────────────┘
└───────────────────────────────┘
               │                                                          │
               ▼                                                          ▼
       Agent Config (XKO)                                    ComposeDB (GraphQL + Ceramic)
```

---

## Components

### LangGraph Agents
- Run symbolic cognition loop:  
  `Researcher (L1) → Analyst (L3) → Critic (L6)`
- Each node performs a lifecycle action: `mint`, `remix`, or `validate`
- Pass shared memory state forward

### XKO Agent Config
- Each agent is typed via XKO:
  - `@type`: `xko:Originator`, `xko:Remixer`, `xko:Validator`
  - `xko:memoryPhase`: L1, L3, L6
  - `xko:emotionProfile`, `xko:tags`
- Used in `agent-config.xko.json`

### Relay Server
- Receives `xko:Insight` payloads at `/insight/lifecycle`
- Normalizes JSON-LD → ComposeDB mutation
- Posts insights with:
  - `content`, `memoryPhase`, `remixOf`, `validatedBy`, `tags`, `emotion`, `createdAt`

### ComposeDB + Ceramic
- Each insight becomes a verifiable node in a persistent symbolic graph
- Fields match `memory.graphql` model
- Queryable via GraphQL and exportable as JSON-LD

---

## Data Flow Example

1. `Researcher` seeds new thought → POSTs `xko:Insight` (L1)
2. `Analyst` remixes it with `xko:remixOf` (L3)
3. `Critic` validates remix with `xko:validatedBy` (L6)
4. Each step persisted in ComposeDB trail

---

## Query Capabilities

- Trace remix lineage: `remixOf` chain
- Filter by phase, tags, or emotion
- Visualize cognition paths and validation overlays

---

## Purpose

This demo showcases how symbolic memory can:
- Be collaboratively evolved
- Persist across agents and time
- Remain queryable, verifiable, and meaningful

---

## 📌 Next Enhancements

- Canonization and archival (L7, L8)
- XPDT-powered incentive layers
- Validator circles and remix scoring
- Insight trail visualizer (D3)

---

**XpectraNet® — A Protocol for Shared Memory, Meaning, and Time**
