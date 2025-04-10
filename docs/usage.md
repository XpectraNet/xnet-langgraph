
# Insight Lifecycle Demo – Deployment & Testing Guide

This guide helps you set up and test the full LangGraph × XpectraNet × ComposeDB stack to experience symbolic memory with remix lineage, validation, and decentralized storage.


---

## 🧩 Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **Node.js v18+**
- **npm**
- **Ceramic CLI** → `npm install -g @composedb/cli`
- **Git**
- **Ceramic Daemon** (Clay testnet node or local devnet)
- (Optional) Docker (for containerized Ceramic or graph tools)

> ℹ️ You’ll also need an authenticated DID to write to ComposeDB (use `composedb did:authenticate`)

---

## 📦 Installation & Setup

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

Create your `.env` if needed:
```bash
cp .env.example .env
```

---

### 4. Deploy the Insight Model to ComposeDB

Install the Ceramic CLI (if not already):
```bash
npm install -g @composedb/cli
```

Start Ceramic daemon (in a separate terminal):

```bash
ceramic daemon --network clay
```

Authenticate with your DID:
```bash
composedb did:authenticate
```

Compile and deploy the model to Ceramic Clay:
```bash
cd relay/compose
composedb composite:compile memory.graphql > model.json
composedb composite:deploy model.json
```

Generate the model-definition.js file (used in memoryLifecycleRelay.js):
```bash
cd relay/compose
composedb composite:codegen model.json --output=./model-definition.js
```

> 🔗 After deployment, your GraphQL endpoint is live at `http://localhost:7007/graphql` or from your Ceramic node provider.

---

### 5. Start the Relay Server

```bash
cd ../
node memoryLifecycleRelay.js
```

> 🔁 Your lifecycle relay is now listening at: `http://localhost:5000/insight/lifecycle`

---

### 6. Run the LangGraph Agent Pipeline

```bash
cd ../langgraph-app
python main.py
```

🧠 This triggers:

- Agent 1: Seeds an insight (`memoryPhase: L1`)
- Agent 2: Transforms the thought (`L3`)
- Agent 3: Aligns it with symbolic weight (`L6`)

Each step is stored in **ComposeDB** — creating a verifiable insight trail.

---

## 🧪 Query & Visualize the Memory Trail

Use the ComposeDB GraphQL endpoint:

```graphql
query {
  insightIndex(first: 5) {
    edges {
      node {
        content
        memoryPhase
        emotion
        remixOf
        validatedBy
        tags
        createdAt
      }
    }
  }
}
```

> You can also visualize trails using D3.js by linking `id` and `remixOf`.

---

## ✅ Successful Run Checklist

✔ Node relay is running at `http://localhost:5000/insight/lifecycle`  
✔ Ceramic daemon is active (testnet or local)  
✔ `memory.graphql` model deployed and registered  
✔ LangGraph flow executed and printed: `Final Insight ID: ...`  
✔ Insights visible in ComposeDB using GraphQL queries  

You're now running a working symbolic memory system for multi-agent cognition.

---

## 📚 Bonus: Understanding memoryPhase

| Phase | Label       | Description                             |
|-------|-------------|-----------------------------------------|
| L1    | Seed        | Original insight or perception          |
| L3    | Transform   | Reframed or structurally evolved thought|
| L6    | Align       | Validated or symbolically confirmed     |
| L7    | Resolve     | Canonized insight (finalized)           |
| L8    | Close       | Archived insight                        |

---

**XpectraNet® — A Protocol for Shared Memory, Meaning, and Time**

Built for memory. Anchored in thought. Powered by XPDT.
