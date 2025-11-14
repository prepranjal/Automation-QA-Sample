wrapstore_automation_py/
├── .env
├── .project
├── .pydevproject
├── behave.ini
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
├── __init__.py
│
├── .settings/
│   ├── org.eclipse.core.resources.prefs
│
├── core/
│   ├── config_reader.py
│   ├── driver_factory.py
│   ├── hooks.py
│   ├── __init__.py
│
├── data/
│   ├── config.yaml
│   ├── test_data.py
│   ├── __init__.py
│
├── features/
│   ├── add_to_cart.feature
│   ├── environment.py
│   ├── __init__.py
│
├── locators/
│   ├── cart_page_locators.py
│   ├── category_page_locators.py
│   ├── home_page_locators.py
│   ├── product_page_locators.py
│   ├── static_locators.py
│   ├── store_page_locators.py
│   ├── __init__.py
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── category_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── store_page.py
│   ├── __init__.py
│
├── reports/
│   ├── allure-reports/
│
├── runners/
│   ├── ci.yml
│   ├── run_behave.sh
│   ├── run_pytest.sh
│
├── steps/
│   ├── cart_steps.py
│   ├── category_steps.py
│   ├── home_steps.py
│   ├── product_steps.py
│   ├── store_steps.py
│   ├── test_steps.py
│   ├── __init__.py
│
├── tests/
│   ├── test_add_to_cart_flow.py
│   ├── __init__.py
│
└── utils/
    ├── action_util.py
    ├── allure_listener.py
    ├── assert_util.py
    ├── logger_util.py
    ├── retry_util.py
    ├── wait_util.py
    ├── __init__.py
