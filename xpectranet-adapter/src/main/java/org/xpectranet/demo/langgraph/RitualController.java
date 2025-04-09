package org.xpectranet.demo.langgraph;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/ritual")
public class RitualController {

    @Autowired
    private XpectraNetLangGraphAdapter adapter;

    @PostMapping("/mint")
    public ResponseEntity<String> mint(@RequestBody Map<String, Object> payload) {
        Map<String, Object> insight = (Map<String, Object>) payload.get("insight");
        return adapter.mintInsight(
            (String) payload.get("agentId"),
            (String) payload.get("layer"),
            (String) insight.get("content"),
            (String) insight.get("emotion"),
            ((java.util.List<String>) insight.get("tags")).toArray(new String[0]),
            (String) insight.get("originType")
        );
    }

    @PostMapping("/remix")
    public ResponseEntity<String> remix(@RequestBody Map<String, Object> payload) {
        Map<String, Object> insight = (Map<String, Object>) payload.get("insight");
        return adapter.remixInsight(
            (String) payload.get("agentId"),
            (String) payload.get("layer"),
            (String) insight.get("content"),
            (String) insight.get("emotion"),
            (String) insight.get("remixOf"),
            ((java.util.List<String>) insight.get("tags")).toArray(new String[0])
        );
    }

    @PostMapping("/validate")
    public ResponseEntity<String> validate(@RequestBody Map<String, Object> payload) {
        Map<String, Object> insight = (Map<String, Object>) payload.get("insight");
        return adapter.validateInsight(
            (String) payload.get("agentId"),
            (String) insight.get("validatedId"),
            (String) insight.get("emotion")
        );
    }
} 
