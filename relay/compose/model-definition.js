// model-definition.js
// Exported model from composedb composite:compile

exports.definition = {
  models: {
    Insight: "kjzl6hvfrbw6c6xxxyourmodelidhere",
  },
  definition: {
    name: "Insight",
    version: "1.0",
    description: "Symbolic insight model for XpectraNet lifecycle memory",
    schema: {
      type: "object",
      properties: {
        content: { type: "string" },
        memoryPhase: { type: "string" },
        emotion: { type: "string" },
        remixOf: { type: "string" },
        validatedBy: {
          type: "array",
          items: { type: "string" }
        },
        tags: {
          type: "array",
          items: { type: "string" }
        },
        createdAt: { type: "string", format: "date-time" }
      },
      required: ["content", "memoryPhase"]
    }
  }
};
