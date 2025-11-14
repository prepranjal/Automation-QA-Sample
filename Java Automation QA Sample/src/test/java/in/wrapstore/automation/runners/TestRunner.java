package in.wrapstore.automation.runners;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;
import org.testng.annotations.Listeners;
import in.wrapstore.automation.listeners.AllureListener;


@CucumberOptions(
    features = "src/test/resources/features",
    glue = {"in.wrapstore.automation.stepDefinitions"},
    		plugin = {
    			    "pretty",
    			    "html:target/cucumber-reports.html",
    			    "json:target/cucumber.json",
    			    "timeline:target/test-timeline",
    			    "io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm"
    			},

    monochrome = true
)
@Listeners(AllureListener.class)
public class TestRunner extends AbstractTestNGCucumberTests {
}
