# GraphQL Queries – Symbolic Insight Memory

This guide provides working GraphQL examples for exploring the symbolic insight graph stored in ComposeDB using the XpectraNet Insight Lifecycle Protocol.

---

## 🧠 Field Reference

| Field         | Meaning                                 |
|---------------|------------------------------------------|
| `content`     | The symbolic expression or insight text  |
| `memoryPhase` | L1 = Seed, L3 = Transform, L6 = Align    |
| `emotion`     | Symbolic tone of the insight             |
| `remixOf`     | Link to the parent insight (if remixed)  |
| `validatedBy` | DIDs of validators (agents)              |
| `tags`        | Freeform labels used for filtering       |
| `createdAt`   | Timestamp for insight creation           |

---

## 📥 Query: All Recent Insights

```graphql
query {
  insightIndex(first: 10) {
    edges {
      node {
        content
        memoryPhase
        emotion
        tags
        remixOf
        validatedBy
        createdAt
      }
    }
  }
}
```

---

## 🔎 Query: By Symbolic Memory Phase (L1, L3, L6)

```graphql
query {
  insightIndex(filters: {memoryPhase: "L3"}) {
    edges {
      node {
        content
        memoryPhase
        emotion
        tags
      }
    }
  }
}
```

---

## 🧬 Query: Explore Remix Lineage

```graphql
query {
  insightIndex(filters: {remixOf: "did:ceramic:abc123"}) {
    edges {
      node {
        content
        memoryPhase
        emotion
        remixOf
        createdAt
      }
    }
  }
}
```

---

## ✅ Query: Validated Insights

```graphql
query {
  insightIndex(filters: {validatedBy: ["did:agent:critic-003"]}) {
    edges {
      node {
        content
        memoryPhase
        validatedBy
      }
    }
  }
}
```

---

## 🏷️ Query: Insights by Tags or Emotional Alignment

```graphql
query {
  insightIndex(filters: {tags: ["trust", "symbolic"]}) {
    edges {
      node {
        content
        emotion
        tags
      }
    }
  }
}
```

---

## 🧠 Optional: Canonized Insight Retrieval (L7)

```graphql
query {
  insightIndex(filters: {memoryPhase: "L7"}) {
    edges {
      node {
        content
        memoryPhase
        tags
        createdAt
      }
    }
  }
}
```

---

## 🔐 ComposeDB Access Notes

- Queries run against your GraphQL endpoint from deployed `memory.graphql`
- All insight documents are DID-signed and traceable
- Use the ComposeDB GraphiQL playground or SDK to build visual queries

---

**XpectraNet® — Symbolic Memory for Agentic Collaboration**
