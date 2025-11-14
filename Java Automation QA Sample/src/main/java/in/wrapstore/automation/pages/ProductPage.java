package in.wrapstore.automation.pages;

import in.wrapstore.automation.data.TestData;
import in.wrapstore.automation.locators.StaticLocators;
import in.wrapstore.automation.utils.*;
import org.openqa.selenium.support.ui.Select;

public class ProductPage extends BasePage {

    /** Opens Batman Toon Glass Case product */
    public void openBatmanToonProduct() {
        LoggerUtil.info("Opening Batman Toon Glass Case product");

        WaitUtil.waitForClickability(driver, StaticLocators.PRODUCT_BATMAN_TOON, 10);
        click(StaticLocators.PRODUCT_BATMAN_TOON);

        AssertUtil.verifyContains(
                getPageTitle().toLowerCase(),
                "batman",
                "Batman Toon Glass Case product page did not open successfully."
        );
    }

    /** Selects Samsung → Galaxy S24 Ultra as brand and model */
    public void selectBatmanToonPhoneModel() {
        LoggerUtil.info("Selecting Brand: " + TestData.BRAND + " and Model: " + TestData.MODEL);

        WaitUtil.waitForVisibility(driver, StaticLocators.DROPDOWN_BRAND, 10);
        Select brandSelect = new Select(find(StaticLocators.DROPDOWN_BRAND));
        brandSelect.selectByVisibleText(TestData.BRAND);

        AssertUtil.verifyEquals(
                brandSelect.getFirstSelectedOption().getText(),
                TestData.BRAND,
                "Phone brand selection failed."
        );

        WaitUtil.waitForVisibility(driver, StaticLocators.DROPDOWN_MODEL, 10);
        Select modelSelect = new Select(find(StaticLocators.DROPDOWN_MODEL));
        modelSelect.selectByVisibleText(TestData.MODEL);

        AssertUtil.verifyEquals(
                modelSelect.getFirstSelectedOption().getText(),
                TestData.MODEL,
                "Phone model selection failed."
        );

        LoggerUtil.info("Successfully selected " + TestData.BRAND + " → " + TestData.MODEL);
    }

    /** Clicks Add to Cart */
    public void addToCart() {
        LoggerUtil.info("Clicking Add to Cart button");
        WaitUtil.waitForClickability(driver, StaticLocators.ADD_TO_CART_BTN, 10);
        click(StaticLocators.ADD_TO_CART_BTN);
    }
}
