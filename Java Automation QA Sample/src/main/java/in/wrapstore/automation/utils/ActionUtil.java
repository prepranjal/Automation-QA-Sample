package in.wrapstore.automation.utils;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.Select;

public class ActionUtil {

    public static void click(WebDriver driver, By locator) {
        driver.findElement(locator).click();
    }

    public static void type(WebDriver driver, By locator, String text) {
        driver.findElement(locator).clear();
        driver.findElement(locator).sendKeys(text);
    }

    public static void selectByVisibleText(WebDriver driver, By locator, String text) {
        new Select(driver.findElement(locator)).selectByVisibleText(text);
    }
}
