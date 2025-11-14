package in.wrapstore.automation.utils;

import java.time.Duration;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.*;

public class WaitUtil {

    public static void waitForVisibility(WebDriver driver, By locator, int timeout) {
        new WebDriverWait(driver, Duration.ofSeconds(timeout))
                .until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    public static void waitForClickability(WebDriver driver, By locator, int timeout) {
        new WebDriverWait(driver, Duration.ofSeconds(timeout))
                .until(ExpectedConditions.elementToBeClickable(locator));
    }
    public static void waitForTitleContains(WebDriver driver, String title, int timeout) {
        new WebDriverWait(driver, Duration.ofSeconds(timeout))
                .until(ExpectedConditions.titleContains(title));
    }

}
