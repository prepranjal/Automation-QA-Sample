package in.wrapstore.automation.listeners;

import io.qameta.allure.Allure;
import io.qameta.allure.model.Status;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import java.io.File;
import java.io.FileInputStream;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import in.wrapstore.automation.core.DriverFactory;


public class AllureListener implements ITestListener {

    @Override
    public void onStart(ITestContext context) {
        createAllureEnvironmentFile();
    }

    private void createAllureEnvironmentFile() {
        try {
            Path resultsDir = Paths.get("allure-results");
            if (!Files.exists(resultsDir)) {
                Files.createDirectories(resultsDir);
            }

            try (FileWriter writer = new FileWriter(resultsDir.resolve("environment.properties").toFile())) {
                writer.write("Browser=Chrome\n");
                writer.write("Environment=QA\n");
                writer.write("Platform=Windows 10\n");
                writer.write("Framework=Wrapstore Automation\n");
            }

            try (FileWriter executor = new FileWriter(resultsDir.resolve("executor.json").toFile())) {
                executor.write("{\n" +
                        "  \"name\": \"Maven Test Execution\",\n" +
                        "  \"type\": \"maven\",\n" +
                        "  \"buildOrder\": 1,\n" +
                        "  \"buildName\": \"Wrapstore Automation Run\",\n" +
                        "  \"reportUrl\": \"\",\n" +
                        "  \"buildUrl\": \"\"\n" +
                        "}");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onTestFailure(ITestResult result) {
        Allure.step("❌ Test Failed: " + result.getName(), Status.FAILED);

        try {
            File screenshot = ((TakesScreenshot) in.wrapstore.automation.core.DriverFactory.getDriver())
                    .getScreenshotAs(OutputType.FILE);
            Allure.addAttachment("Screenshot on Failure", new FileInputStream(screenshot));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onTestSuccess(ITestResult result) {
        Allure.step("✅ Test Passed: " + result.getName(), Status.PASSED);
    }


}
