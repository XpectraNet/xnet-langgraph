# 🧠 Symbolic Memory Lifecycle — XpectraNet Demo (L1 → L3 → L6)

This demo simulates how insights evolve through structured symbolic memory phases —  
minted by researchers, remixed by analysts, and validated by critics — using the Xpectra Knowledge Ontology (XKO) and stored in ComposeDB.

---

## 🔄 Agent Loop (LangGraph)

```
Researcher (L1)
   ↓
Analyst (L3)
   ↓
Critic (L6)
   ↺
   ↳ Analyst (L3) (loop continues...)
```

---

## 🧠 Agent Roles (Defined via XKO)

| Role       | XKO Type           | Phase | Action           |
|------------|--------------------|--------|------------------|
| Researcher | xko:Originator     | L1     | mint_insight()   |
| Analyst    | xko:Remixer        | L3     | remix_insight()  |
| Critic     | xko:Validator      | L6     | validate_insight() |

Each role is defined via `agent-config.xko.json` using XKO ontology tags.

---

## ⛓️ Memory Evolution Flow

1. **Seed**: `Researcher` generates insight → `memoryPhase: xko:L1`
2. **Remix**: `Analyst` reframes it → `xko:remixOf: previous_id`, `memoryPhase: xko:L3`
3. **Validate**: `Critic` affirms remix → `xko:validatedBy`, `memoryPhase: xko:L6`
4. **Repeat**: Analyst continues remix trail with deeper interpretation

---

## 🧬 Insight Graph Stored in ComposeDB

- Schema: `memory.graphql` defines an `xko:Insight`
- Each lifecycle POST is routed through:
  - `POST /insight/lifecycle`
  - → Relay (Node.js)
  - → ComposeDB mutation

---

## ✅ Why This Matters

This symbolic memory lifecycle:
- Encodes provenance (`remixOf`)
- Embeds trust (`validatedBy`)
- Anchors emotion, layer, and time
- Evolves meaning — not just state

---

## ✨ Example Export

Exported trail (via `scripts/export_trail_snapshot.py`) outputs a JSON-LD snapshot:

```json
{
  "@context": "https://xpectranet.org/xko#",
  "@type": "xko:Insight",
  "xko:memoryPhase": "xko:L3",
  "xko:remixOf": "did:ceramic:xyz...",
  "xko:validatedBy": ["did:agent:x0-critic"]
}
```

---

**This is not just memory.  
It is cognition, with structure.**

**XpectraNet® — Evolving Thought Through Symbolic Trails**
