from utilities import XLutilities
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig
from pageObject.UserLogin_Page import UserLoginClass
from selenium import webdriver


class Test_login_DDT_003:
    baseURL = ReadConfig.get_application_url()
    path = ".\\TestData\\Test Data.xlsx"
    log = LogGen.loggen()


    def test_login_DDT(self, setup):
        self.log.info("Test_login_DDT_003 is starting ")
        self.log.info("Verifying Test_login_DDT_003")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = UserLoginClass(self.driver)
        self.rows = XLutilities.getRowCount(self.path, "Sheet1")
        LoginStatus = []

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
            self.lp.sign_out()
            self.log.info("Clicking on login button")
