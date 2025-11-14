package in.wrapstore.automation.stepDefinitions;

import in.wrapstore.automation.data.TestData;
import in.wrapstore.automation.pages.*;
import in.wrapstore.automation.utils.LoggerUtil;
import io.cucumber.java.en.*;

public class TestSteps {

    private final HomePage homePage = new HomePage();
    private final StorePage storePage = new StorePage();
    private final CategoryPage categoryPage = new CategoryPage();
    private final ProductPage productPage = new ProductPage();
    private final CartPage cartPage = new CartPage();

    @Given("user is on the Wrapstore homepage")
    public void user_is_on_the_wrapstore_homepage() {
        LoggerUtil.info("STEP: User navigates to Wrapstore homepage");
        homePage.openHomePage();
        homePage.verifyHomePageLoaded();
    }

    @When("user opens the Store page")
    public void user_opens_the_store_page() {
        LoggerUtil.info("STEP: User opens Store page");
        storePage.openStorePage();
    }

    @And("user opens the Armour Glass Case category")
    public void user_opens_the_armour_glass_case_category() {
        LoggerUtil.info("STEP: User opens Armour Glass Case category");
        categoryPage.openArmourGlassCategory();
    }

    @And("user selects Batman Toon Glass Case phone model")
    public void user_selects_batman_toon_glass_case_phone_model() {
        LoggerUtil.info("STEP: User selects Batman Toon Glass Case product and chooses model");
        productPage.openBatmanToonProduct();
        productPage.selectBatmanToonPhoneModel();
    }

    @Then("user clicks Add to Cart and is redirected to the Cart page")
    public void user_clicks_add_to_cart_and_is_redirected_to_the_cart_page() {
        LoggerUtil.info("STEP: User clicks Add to Cart and validates Cart page");
        cartPage.clickAddToCartAndNavigateToCartPage();
    }
}
