// memoryLifecycleRelay.js — XKO-compliant relay for symbolic memory lifecycle
// Accepts POST /insight/lifecycle → transforms XKO JSON-LD into ComposeDB mutation

const express = require("express");
const bodyParser = require("body-parser");
const { request } = require("graphql-request");

const app = express();
app.use(bodyParser.json());

// ComposeDB GraphQL endpoint (testnet: Clay)
const GRAPHQL_ENDPOINT = "https://ceramic-clay.3boxlabs.com";

// Simple GraphQL mutation for creating an insight document
const CREATE_INSIGHT_MUTATION = `
  mutation CreateInsight($input: CreateInsightInput!) {
    createInsight(input: $input) {
      document {
        id
        content
        memoryPhase
        remixOf
        validatedBy
        tags
        emotion
        createdAt
      }
    }
  }
`;

app.post("/insight/lifecycle", async (req, res) => {
  try {
    const payload = req.body;

    // Step 1: Validate that required XKO fields exist
    if (!payload["xko:content"] || !payload["xko:memoryPhase"] || !payload["xko:createdAt"]) {
      return res.status(400).json({ error: "Missing required xko fields." });
    }

    // Step 2: Normalize the XKO fields for ComposeDB schema
    const insight = {
      content: payload["xko:content"],
      memoryPhase: payload["xko:memoryPhase"],
      remixOf: payload["xko:remixOf"] || null,
      validatedBy: payload["xko:validatedBy"] || [],
      emotion: payload["xko:emotion"] || null,
      tags: payload["xko:tags"] || [],
      createdAt: payload["xko:createdAt"]
    };

    // Step 3: Send to ComposeDB
    const variables = { input: { content: insight } };
    const result = await request(GRAPHQL_ENDPOINT + "/graphql", CREATE_INSIGHT_MUTATION, {
      input: { content: insight }
    });

    // Step 4: Respond with symbolic memory node (as JSON-LD)
    res.json({
      "@context": "https://xpectranet.org/xko#",
      "@type": "xko:Insight",
      ...payload,
      id: result?.createInsight?.document?.id || null
    });
  } catch (err) {
    console.error("Relay error:", err);
    res.status(500).json({ error: "Relay failed to process memory lifecycle." });
  }
});

// Start server
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`🧠 Relay listening at http://localhost:${PORT}/insight/lifecycle`);
});