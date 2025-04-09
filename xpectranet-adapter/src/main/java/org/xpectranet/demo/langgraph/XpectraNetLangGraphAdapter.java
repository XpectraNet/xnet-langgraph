
package org.xpectranet.demo.langgraph;

import java.util.Map;
import java.util.UUID;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class XpectraNetLangGraphAdapter {

    private static final String RITUAL_ENDPOINT = "https://api.xpectranet.org/api/ritual/perform";
    private final RestTemplate restTemplate;

    public XpectraNetLangGraphAdapter(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public ResponseEntity<String> mintInsight(String agentId, String layer, String content, String emotion, String[] tags, String originType) {
        Map<String, Object> payload = Map.of(
            "agentId", agentId,
            "action", "mint",
            "layer", layer,
            "insight", Map.of(
                "content", content,
                "emotion", emotion,
                "tags", tags,
                "originType", originType
            ),
            "xpdtStake", 1.0
        );

        return postToXpectraNet(payload);
    }

    public ResponseEntity<String> remixInsight(String agentId, String layer, String content, String emotion, String remixOfId, String[] tags) {
        Map<String, Object> payload = Map.of(
            "agentId", agentId,
            "action", "remix",
            "layer", layer,
            "insight", Map.of(
                "content", content,
                "emotion", emotion,
                "remixOf", remixOfId,
                "tags", tags
            ),
            "xpdtStake", 1.0
        );

        return postToXpectraNet(payload);
    }

    public ResponseEntity<String> validateInsight(String agentId, String insightId, String emotion) {
        Map<String, Object> payload = Map.of(
            "agentId", agentId,
            "action", "validate",
            "layer", "L6",
            "insight", Map.of(
                "validatedId", insightId,
                "emotion", emotion
            ),
            "xpdtStake", 1.0
        );

        return postToXpectraNet(payload);
    }

    public ResponseEntity<String> canonizeInsight(String agentId, String insightId, String[] validatorComments) {
        Map<String, Object> payload = Map.of(
            "agentId", agentId,
            "action", "canonize",
            "layer", "L7",
            "insight", Map.of(
                "insightId", insightId,
                "validatorComments", validatorComments
            ),
            "xpdtStake", 5.0
        );

        return postToXpectraNet(payload);
    }

    public ResponseEntity<String> archiveInsight(String agentId, String insightId, String reason) {
        Map<String, Object> payload = Map.of(
            "agentId", agentId,
            "action", "archive",
            "layer", "L8",
            "insight", Map.of(
                "insightId", insightId,
                "reason", reason
            ),
            "xpdtStake", 1.0
        );

        return postToXpectraNet(payload);
    }

    private ResponseEntity<String> postToXpectraNet(Map<String, Object> payload) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Map<String, Object>> request = new HttpEntity<>(payload, headers);

        return restTemplate.exchange(
            RITUAL_ENDPOINT,
            HttpMethod.POST,
            request,
            String.class
        );
    }
}
