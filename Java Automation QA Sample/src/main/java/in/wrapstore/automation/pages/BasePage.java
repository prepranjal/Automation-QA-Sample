package in.wrapstore.automation.pages;

import in.wrapstore.automation.core.DriverFactory;
import in.wrapstore.automation.utils.LoggerUtil;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class BasePage {

    protected WebDriver driver;

    public BasePage() {
        this.driver = DriverFactory.getDriver();
    }

    /** Generic click method */
    protected void click(By locator) {
        LoggerUtil.info("Clicking element: " + locator);
        driver.findElement(locator).click();
    }

    /** Generic type method */
    protected void type(By locator, String text) {
        LoggerUtil.info("Typing into element: " + locator + " | Text: " + text);
        WebElement element = driver.findElement(locator);
        element.clear();
        element.sendKeys(text);
    }

    /** Generic getText method */
    protected String getText(By locator) {
        String text = driver.findElement(locator).getText();
        LoggerUtil.info("Reading text from element: " + locator + " | Value: " + text);
        return text;
    }

    /** Generic wait until visible (used only if necessary in special cases) */
    protected WebElement find(By locator) {
        return driver.findElement(locator);
    }

    public String getPageTitle() {
        String title = driver.getTitle();
        LoggerUtil.info("Current Page Title: " + title);
        return title;
    }

    public String getCurrentUrl() {
        String url = driver.getCurrentUrl();
        LoggerUtil.info("Current URL: " + url);
        return url;
    }
}
