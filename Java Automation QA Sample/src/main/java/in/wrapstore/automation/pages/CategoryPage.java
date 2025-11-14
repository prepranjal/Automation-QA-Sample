package in.wrapstore.automation.pages;

import in.wrapstore.automation.locators.StaticLocators;
import in.wrapstore.automation.utils.AssertUtil;
import in.wrapstore.automation.utils.LoggerUtil;
import in.wrapstore.automation.utils.WaitUtil;

public class CategoryPage extends BasePage {

    /** Opens the Armour Glass Case category page and validates navigation */
    public void openArmourGlassCategory() {
        LoggerUtil.info("Opening Armour Glass Case category page");

        WaitUtil.waitForClickability(driver, StaticLocators.CATEGORY_ARMOUR_GLASS, 10);
        click(StaticLocators.CATEGORY_ARMOUR_GLASS);

        AssertUtil.verifyContains(
                getPageTitle().toLowerCase(),
                "armour glass",
                "Armour Glass Case category page did not open successfully."
        );

        LoggerUtil.info("Armour Glass Case category page opened successfully");
    }
}
