// memoryLifecycleRelay.js
// A symbolic relay that receives insight lifecycle events from LangGraph agents
// and stores them into ComposeDB using Ceramic's GraphQL API

const express = require('express');
const { ComposeClient } = require('@composedb/client');
const { definition } = require('./compose/model-definition.js'); // output from composedb composite:compile

const app = express();
const PORT = 5000;

// Middleware to parse JSON payloads
app.use(express.json());

// Initialize ComposeClient
const compose = new ComposeClient({
  ceramic: 'https://ceramic-clay.3boxlabs.com', // Ceramic Clay testnet endpoint
  definition,
});

// Optional: you can authenticate DID if needed
// compose.setDID(...)


// POST /insight/lifecycle — receives symbolic insight data
app.post('/insight/lifecycle', async (req, res) => {
  try {
    const {
      content,
      memoryPhase,
      emotion,
      remixOf,
      validatedBy,
      tags,
    } = req.body;

    // Basic validation
    if (!content || !memoryPhase) {
      return res.status(400).json({ error: 'Missing required fields: content, memoryPhase' });
    }

    // Prepare input payload for ComposeDB
    const input = {
      content,
      memoryPhase,
      emotion: emotion || null,
      remixOf: remixOf || null,
      validatedBy: validatedBy || [],
      tags: tags || [],
      createdAt: new Date().toISOString(),
    };

    // Call the createInsight mutation using ComposeClient
    const response = await compose.executeQuery(`
      mutation CreateInsight($input: CreateInsightInput!) {
        createInsight(input: $input) {
          document {
            id
            content
            memoryPhase
            emotion
          }
        }
      }
    `, { input });

    // Handle ComposeDB response
    const created = response?.data?.createInsight?.document;
    if (!created) {
      return res.status(500).json({ error: 'Failed to store insight in ComposeDB', details: response });
    }

    console.log('✅ Insight stored:', created);
    res.status(201).json({ success: true, id: created.id, memoryPhase: created.memoryPhase });

  } catch (err) {
    console.error('❌ Error in lifecycle handler:', err);
    res.status(500).json({ error: 'Server error', details: err.message });
  }
});

// Health check endpoint
app.get('/', (req, res) => {
  res.send('🧠 Insight Lifecycle Relay is live');
});

// Start the server
app.listen(PORT, () => {
  console.log(`🚀 Relay listening at http://localhost:${PORT}/insight/lifecycle`);
});
