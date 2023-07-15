import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
        print("Lunching Firefox Browser")
    elif browser == "chrome":
        driver = webdriver.Chrome()
        print("Lunching Chrome Browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Lunching Edge Browser")
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(params=[
    ("lukeshade@gmail.com", "Test@123", "Pass"),
    ("lukeshade@12gmail.com", "Test@123", "Fail"),
    ("lukeshade@gmail.com", "Test@1234", "Fail"),
    ("lukeshade@12gmail.com", "Test@1234", "Fail")
])
def data_for_login(request):
    return request.param
