package in.wrapstore.automation.core;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

/**
 * Manages WebDriver instances for all threads.
 * Handles browser initialization and teardown for Cucumber + TestNG.
 */
public class DriverFactory {

    // Thread-safe WebDriver instance
    private static final ThreadLocal<WebDriver> tlDriver = new ThreadLocal<>();

    /** Returns the WebDriver instance for the current thread */
    public static WebDriver getDriver() {
        return tlDriver.get();
    }

    /** Initializes the WebDriver based on config values */
    public static void initDriver(String browserName) {
        WebDriver driver;

        if (browserName == null || browserName.isEmpty()) {
            browserName = ConfigReader.getBrowser(); // fallback to config file
        }

        boolean headless = ConfigReader.isHeadless();

        switch (browserName.toLowerCase()) {
            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                driver = new FirefoxDriver();
                break;

            case "edge":
                WebDriverManager.edgedriver().setup();
                driver = new EdgeDriver();
                break;

            default:
                WebDriverManager.chromedriver().setup();
                ChromeOptions options = new ChromeOptions();
                if (headless) {
                    options.addArguments("--headless=new");
                    options.addArguments("--disable-gpu");
                }
                options.addArguments("--start-maximized");
                options.addArguments("--disable-notifications");
                options.addArguments("--remote-allow-origins=*");
                driver = new ChromeDriver(options);
                break;
        }

        tlDriver.set(driver);
        driver.manage().window().maximize();
    }

    /** Quits and cleans up the WebDriver instance */
    public static void quitDriver() {
        WebDriver driver = tlDriver.get();
        if (driver != null) {
            driver.quit();
            tlDriver.remove();
        }
    }
}
