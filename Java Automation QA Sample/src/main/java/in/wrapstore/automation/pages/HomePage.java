package in.wrapstore.automation.pages;

import in.wrapstore.automation.data.TestData;
import in.wrapstore.automation.utils.AssertUtil;
import in.wrapstore.automation.utils.LoggerUtil;

public class HomePage extends BasePage {

    /** Opens the Wrapstore Home Page */
    public void openHomePage() {
        LoggerUtil.info("Opening Wrapstore Home Page: " + TestData.BASE_URL);
        driver.get(TestData.BASE_URL);

        AssertUtil.verifyContains(
                getPageTitle().toLowerCase(),
                "wrapstore",
                "Home page did not open successfully."
        );
    }

    /** Validates if the Home Page is loaded successfully */
    public void verifyHomePageLoaded() {
        LoggerUtil.info("Verifying if Home Page is loaded");
        AssertUtil.verifyContains(
                getPageTitle().toLowerCase(),
                "wrapstore",
                "Home page title verification failed — Page not loaded correctly."
        );
        LoggerUtil.info("Home Page loaded successfully");
    }
}
