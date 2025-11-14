package in.wrapstore.automation.locators;

import org.openqa.selenium.By;

public class StaticLocators {

    // -------------------------------
    // Home Page
    // -------------------------------
    public static final By STORE_LINK = By.linkText("Store");

    // -------------------------------
    // Store Page
    // -------------------------------
    public static final By CATEGORY_ARMOUR_GLASS = By.xpath("//img[@alt='Armour Glass Case']");

    // -------------------------------
    // Category Page
    // -------------------------------
    public static final By PRODUCT_BATMAN_TOON = By.xpath("//h2[contains(text(),'Batman Toon Glass Case')]");

    // -------------------------------
    // Product Page
    // -------------------------------
    public static final By DROPDOWN_BRAND = By.id("wrapstore_brand");
    public static final By DROPDOWN_MODEL = By.id("wrapstore_device");
    public static final By ADD_TO_CART_BTN = By.cssSelector("button.single_add_to_cart_button[name='add-to-cart']");


    // -------------------------------
    // Cart Page
    // -------------------------------
    public static final By CART_TITLE = By.cssSelector("h1.entry-title");
}
