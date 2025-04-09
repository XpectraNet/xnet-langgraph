
# Insight Lifecycle Demo – Deployment & Testing Guide

This guide helps you set up and test the full LangGraph × XpectraNet × ComposeDB stack to experience symbolic memory with remix lineage, validation, and decentralized storage.

---

## 🧩 Prerequisites

- Python 3.8+
- Node.js 18+
- Ceramic CLI (`npm install -g @composedb/cli`)
- Git
- Docker (optional, for Ceramic devnet)

---

## 🛠️ Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/XpectraNet/insight-lifecycle-demo.git
cd insight-lifecycle-demo
```

---

### 2. Install LangGraph Agent Dependencies

```bash
cd langgraph-app
pip install -r requirements.txt
# or manually:
pip install openai langchain langgraph requests
```

---

### 3. Install the Insight-to-Compose Relay

```bash
cd ../relay
npm install
```

Set up your `.env` (optional, depending on ComposeClient config):
```bash
cp .env.example .env
```

---

### 4. Deploy the Insight Model to ComposeDB

Start Ceramic daemon (in a separate terminal):

```bash
ceramic daemon --network clay
```

Authenticate:
```bash
composedb did:authenticate
```

Deploy the model:
```bash
cd relay/compose
composedb composite:compile memory.graphql > model.json
composedb composite:deploy model.json
```

---

### 5. Start the Relay Server

```bash
cd ../
node memoryLifecycleRelay.js
```

The server should listen on `http://localhost:5000`

---

### 6. Run the LangGraph Agent Pipeline

```bash
cd ../langgraph-app
python main.py
```

This triggers:

- Agent 1: seeds an insight (Phase L1)
- Agent 2: transforms insight (L3 remix)
- Agent 3: validates it (L6 alignment)

Each step is sent to the relay → ComposeDB → stored as symbolic memory.

---

## 🧪 Test Your Trail

### Query via GraphQL Playground or ComposeDB endpoint:

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

---

## 🔍 Tips

- For DIDs, use Ceramic’s `did:key` or connect with `@composedb/devtools`
- Customize agents to test different emotional states or memory phase mappings
- Fork the repo and plug into your LangGraph projects

---

**XpectraNet® – Symbolic Memory for Agentic Collaboration**
