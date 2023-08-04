import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLogin_Page import UserLoginClass
from utilities.ReadConfigFile import ReadConfig
from utilities.Logger import LogGen


class Test_UserLogin:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_002(self, setup):
        self.log.info("UserLogin_test_002 start")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("invoking the url")
        self.lp = UserLoginClass(self.driver)
        self.lp.login_link()
        self.log.info("Clicking link")
        self.lp.email(self.username)
        self.log.info("Entering Username")
        self.lp.password(self.password)
        self.log.info("Entering password")
        self.lp.signin_button()
        self.log.info("Clicking on Signin Button")
        self.lp.sign_out()
        self.log.info("Clicking on sign out Button")
        ExpTitle = "Home Page"
        if self.driver.title == ExpTitle:
            self.log.info("Testcases test_login_002 is pass")
            self.driver.save_screenshot(".\\Screenshot\\test_login_002_pass.png")
            assert True
        else:
            self.log.info("Testcases test_login_002 is fail")
            self.driver.save_screenshot(".\\Screenshot\\test_login_002_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_002",
                          attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()
        self.log.info("Testcase test_login_002 is complete")



# driver=webdriver.Firefox()
# driver.get("https://magento.softwaretestingboard.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//div[@class='panel header']//li[@data-label='or']").click()
# driver.find_element(By.ID,"email").send_keys("lukeshade@gmail.com")
# driver.find_element(By.ID,"pass").send_keys("Test@123")
# driver.find_element(By.ID,"send2").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "div[class='panel header'] button[type='button']").click()
# driver.find_element(By.XPATH,"//div[@aria-hidden='false']//li[@data-label='or']").click()
# driver.close()
