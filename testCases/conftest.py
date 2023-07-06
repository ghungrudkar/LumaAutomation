import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.firefox
        print("Lunching Firefox Browser")
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://magento.softwaretestingboard.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def pytest_add_option(parser):
    parser.addoption("--browser")

    @pytest.fixture()
    def browser(request):
        return request.config.getoption("--browser")
