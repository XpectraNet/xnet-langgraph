
# Querying the Insight Graph – GraphQL Guide

This guide provides example GraphQL queries for interacting with your ComposeDB-powered insight graph via the XpectraNet Insight Lifecycle Protocol.

---

## 🔍 1. Fetch All Recent Insights

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

## 🧠 2. Filter by Memory Phase

```graphql
query {
  insightIndex(first: 5, filters: {memoryPhase: "L3"}) {
    edges {
      node {
        content
        memoryPhase
        emotion
      }
    }
  }
}
```

---

## 🌀 3. Explore Remix Lineage

```graphql
query {
  insightIndex(filters: {remixOf: "did:ceramic:your-source-id"}) {
    edges {
      node {
        content
        emotion
        memoryPhase
        remixOf
      }
    }
  }
}
```

---

## ✔️ 4. Filter by Validators

```graphql
query {
  insightIndex(filters: {validatedBy: ["did:your-validator-did"]}) {
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

## 🧾 5. Search by Tags or Emotional Alignment

```graphql
query {
  insightIndex(filters: {tags: ["truth", "symbolic"]}) {
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

## 🛠️ Notes

- Field: `memoryPhase` refers to the symbolic stage (e.g., L1, L3, L6).
- Use `remixOf` to traverse trails or remix ancestry.
- All documents are signed via Ceramic's DID system for traceable authorship.

---

**XpectraNet® – Evolving Memory Through Symbolic Graphs**
