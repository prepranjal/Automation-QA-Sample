package in.wrapstore.automation.pages;

import in.wrapstore.automation.locators.StaticLocators;
import in.wrapstore.automation.utils.AssertUtil;
import in.wrapstore.automation.utils.LoggerUtil;
import in.wrapstore.automation.utils.WaitUtil;

public class StorePage extends BasePage {

    /** Opens the Store page by clicking the Store link in the header */
    public void openStorePage() {
        LoggerUtil.info("Navigating to Store page from Home");

        WaitUtil.waitForClickability(driver, StaticLocators.STORE_LINK, 10);
        click(StaticLocators.STORE_LINK);

        AssertUtil.verifyContains(
                getPageTitle().toLowerCase(),
                "store",
                "Store page did not open successfully."
        );

        LoggerUtil.info("Store page opened successfully");
    }
}
