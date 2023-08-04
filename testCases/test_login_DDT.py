import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities import XLutilities
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig
from pageObject.UserLogin_Page import UserLoginClass
from selenium import webdriver


class Test_login_DDT_003:
    baseURL = ReadConfig.get_application_url()
    path = ".\\TestData\\testData.xlsx"
    log = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.log.info("Test_login_DDT_003 is starting ")
        self.log.info("Verifying Test_login_DDT_003")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = UserLoginClass(self.driver)
        self.rows = XLutilities.getRowCount(self.path, "Sheet1")
        loginStatus = []

        for r in range(2, self.rows + 1):
            self.username = XLutilities.readData(self.path, "Sheet1", r, 1)
            self.password = XLutilities.readData(self.path, "Sheet1", r, 2)
            self.Expected = XLutilities.readData(self.path, "Sheet1", r, 3)
            self.lp.login_link()
            self.log.info("Clicking on login link")
            self.lp.email(self.username)
            self.log.info("entering username")
            self.lp.password(self.password)
            self.log.info("entering password")
            self.lp.signin_button()
            self.log.info("Clicking on submit button")
            self.driver.implicitly_wait(10)

            act_title = self.driver.title
            exp_title = "Home Page"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("Pass")
                    loginStatus.append("Pass")
                    XLutilities.writeData(self.path, "Sheet1", r, 4, "Pass")
                    self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_PASS.png")
                    self.lp.sign_out()
                    time.sleep(2)
                elif self.exp == "Fail":
                    self.log.info("Fail")
                    loginStatus.append("Fail")
                    XLutilities.writeData(self.path, "Sheet1", r, 4, "Fail")
                    self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_FAIL.png")
                    self.lp.sign_out()
                    time.sleep(2)
                elif act_title != exp_title:
                    if self.Exp == "Pass":
                        self.log.info("Fail")
                        loginStatus.append("Fail")
                        XLutilities.writeData(self.path, "Sheet1", r, 4, "Fail")
                        self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_PASS.png")
                        self.driver.refresh()
                    elif self.Exp == "Fail":
                        self.log.info("Pass")
                        loginStatus.append("Pass")
                        XLutilities.writeData(self.path, "Sheet1", r, 4, "Pass")
                        self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_PASS.png")
                        self.driver.refresh()

        if "Fail" not in loginStatus:
            self.log.info("Testcases test_login_DDT_003 is passed")
            self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_PASS.png")
            assert True
        else:
            self.log.info("Testcases test_login_DDT_003 is failed")
            self.driver.save_screenshot(".\\Screenshot\\test_login_DDT_003_FAIL.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_ddt",
                          attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()
        self.log.info("End of Login DDT Test")
        self.log.info("Completed test_Login_DDT_003) ")
