package in.wrapstore.automation.stepDefinitions;

import in.wrapstore.automation.core.DriverFactory;
import io.cucumber.java.Before;
import io.cucumber.java.After;
import io.cucumber.java.AfterAll;
import java.io.IOException;

public class Hooks {

    @Before
    public void setup() {
        DriverFactory.initDriver("chrome");
    }

    @After
    public void teardown() {
        DriverFactory.quitDriver();
    }
    @AfterAll
    public static void generateAllureReport() {
        try {
            // Clean and generate the Allure report
            ProcessBuilder builder = new ProcessBuilder(
                    "cmd.exe", "/c",
                    "allure generate allure-results --clean -o allure-report && start allure serve allure-results"
            );
            builder.inheritIO();
            Process process = builder.start();
            process.waitFor();
            System.out.println("✅ Allure Report generated and opened successfully!");
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            System.err.println("❌ Failed to generate or open Allure report automatically.");
        }
    }
}
