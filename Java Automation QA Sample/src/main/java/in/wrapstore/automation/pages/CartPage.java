package in.wrapstore.automation.pages;

import in.wrapstore.automation.locators.StaticLocators;
import in.wrapstore.automation.utils.AssertUtil;
import in.wrapstore.automation.utils.LoggerUtil;
import in.wrapstore.automation.utils.WaitUtil;

public class CartPage extends BasePage {

    /** Clicks Add to Cart button and validates redirection to the Cart page */
    public void clickAddToCartAndNavigateToCartPage() {
        LoggerUtil.info("Clicking Add to Cart button");

        WaitUtil.waitForClickability(driver, StaticLocators.ADD_TO_CART_BTN, 10);
        click(StaticLocators.ADD_TO_CART_BTN);

        LoggerUtil.info("Waiting for Cart page to load");
        WaitUtil.waitForTitleContains(driver, "Cart", 10);

        String actualTitle = getPageTitle();
        LoggerUtil.info("Validating Cart page title: " + actualTitle);

        AssertUtil.verifyEquals(
                actualTitle,
                "Cart - Premium Phone Cases - WRAPSTORE",
                "Cart page title validation failed."
        );

        LoggerUtil.info("Successfully navigated to Cart page");
    }
}
