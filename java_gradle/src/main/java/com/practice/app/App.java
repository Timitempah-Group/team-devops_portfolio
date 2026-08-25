package com.practice.app;

public class App {
    public String getGreeting() {
        return "Hello from Gradle-built Java, running on JDK 21";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
