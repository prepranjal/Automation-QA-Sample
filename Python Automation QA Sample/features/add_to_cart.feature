Feature: Add BatmanToon product to cart

  Scenario: User adds Batman Toon Armour Glass Case to cart
    Given user is on the Wrapstore homepage
    When user opens the Store page
    And user opens the Armour Glass Case category
    And user selects Batman Toon Glass Case phone model
    Then user clicks Add to Cart and is redirected to the Cart page