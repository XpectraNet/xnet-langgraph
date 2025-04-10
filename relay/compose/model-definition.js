// model-definition.js — XKO-aligned ComposeDB model for Insight lifecycle
// Exported model from composedb composite:compile

exports.definition = {
  models: {
    Insight: "kjzl6hvfrbw6cxyzXKOModelExample1234567890" // replace with actual model ID after deployment
  },
  definition: {
    name: "Insight",
    version: "1.0",
    description: "xko:Insight - A symbolic memory node in XpectraNet",
    schema: {
      type: "object",
      properties: {
        content: { type: "string", xko: "xko:content" },
        memoryPhase: { type: "string", xko: "xko:memoryPhase" },
        emotion: { type: "string", xko: "xko:emotion" },
        remixOf: { type: "string", xko: "xko:remixOf" },
        validatedBy: {
          type: "array",
          items: { type: "string" },
          xko: "xko:validatedBy"
        },
        tags: {
          type: "array",
          items: { type: "string" },
          xko: "xko:tag"
        },
        createdAt: { type: "string", format: "date-time", xko: "xko:timestamp" }
      },
      required: ["content", "memoryPhase", "createdAt"]
    }
  }
}