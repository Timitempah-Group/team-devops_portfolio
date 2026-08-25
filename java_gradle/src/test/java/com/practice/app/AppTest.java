package com.practice.app;

import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class AppTest {
    @Test
    void greetingMentionsGradle() {
        App app = new App();
        assertTrue(app.getGreeting().contains("Gradle"));
    }
}
