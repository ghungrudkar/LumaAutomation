import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLogin_Page import UserLoginClass
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class Test_Login:
    log = LogGen.loggen()
    baseURL = ReadConfig.get_application_url()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_param_004(self, setup, data_for_login):
        self.log.info("TestCase test_login_004 is started")
        self.driver = setup
        self.log.info("Invoking browser")
        self.driver.get(self.baseURL)
        self.log.info("Opening url")
        self.lp = UserLoginClass(self.driver)
        self.lp.login_link()
        self.log.info("Clicking on login link")
        self.lp.email(data_for_login[0])
        self.log.info("Entering email " + data_for_login[0])
        self.lp.password(data_for_login[1])
        self.log.info("Entering password " + data_for_login[1])
        self.lp.signin_button()
        self.log.info("Clicking on Signin button")

        if self.lp.status() == (data_for_login[2] == "Pass"):
            self.log.info("TestCase test_login_param_004 is pass")
            self.driver.save_screenshot(".\\Screenshot\\test_login_004_pass.png")
            assert True
        else:
            self.log.info("TestCase test_login_param_004 is fail")
            self.driver.save_screenshot(".\\Screenshot\\test_login_004_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_param_004",
                          attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()
        self.log.info("TestCase test_login_param_004 is close")
