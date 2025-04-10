# Insight Lifecycle Workflow – Agent Memory Flow Explained

This document explains how the LangGraph-powered agent pipeline simulates symbolic memory through the XpectraNet Insight Lifecycle Protocol and stores it on ComposeDB.

---

## 🔄 What Happens in This Workflow?

This LangGraph-powered flow demonstrates how agents evolve symbolic insights using the **XpectraNet Insight Lifecycle Protocol**.

Each step calls `POST /insight/lifecycle` via dedicated Python hooks (`mint`, `remix`, `validate`) and stores memory into ComposeDB.

---

### 🧠 Step-by-Step Lifecycle

#### 1. 🧪 Researcher Agent
- **Action:** Seeds a new insight
- **Phase:** `memoryPhase: L1`
- **Hook:** `mint_insight()`
- **Output:** Creates a new symbolic thought
- **Tags:** `["seed", "symbolic"]`

#### 2. 🔁 Analyst Agent
- **Action:** Transforms the original insight
- **Phase:** `memoryPhase: L3`
- **Hook:** `remix_insight()`
- **Output:** New interpretation linked by `remixOf`
- **Tags:** `["structure", "cognition"]`

#### 3. ✅ Critic Agent
- **Action:** Validates or aligns the transformed insight
- **Phase:** `memoryPhase: L6`
- **Hook:** `validate_insight()`
- **Output:** Adds symbolic weight + validator signature
- **Tags:** `["validated", "aligned"]`

---

### 📦 Final Result

- All insights are persisted to **ComposeDB**
- Each insight node includes:
  - `content`
  - `emotion`
  - `memoryPhase`
  - `remixOf` or `validatedBy` lineage
- The full memory trail is:
  - ✅ Verifiable
  - 🔍 Queryable
  - 🔁 Evolvable

---

**XpectraNet® — Cognitive Infrastructure for Symbolic Agents**
