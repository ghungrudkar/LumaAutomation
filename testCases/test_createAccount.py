import string
import random

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObject.UserAccount_Page import UserRegistrationClass
from utilities.Logger import LogGen

from utilities.ReadConfigFile import ReadConfig


class Test_CreateAccount:
    log = LogGen.loggen()
    url = ReadConfig.get_application_url()
    password = ReadConfig.get_password()

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_registration_001(self, setup):
        self.driver = setup
        self.log.info("TestCase test_registration_001 is started")
        self.log.info("invoking the browser")
        self.driver.get(self.url)
        self.log.info("opening URL")
        self.rp = UserRegistrationClass(self.driver)
        self.rp.link_registration()
        self.log.info("clicking on registration link")
        self.rp.firstname("Lukesh")
        self.log.info("entering firstname")
        self.rp.lastname("Ade")
        self.log.info("entering lastname")
        self.email = random_generator() + "@gmail.com"
        self.rp.setEmail(self.email)
        self.log.info("entering the email")
        self.rp.password(self.password)
        self.log.info("entering the password")
        self.rp.confirm_password(self.password)
        self.log.info("entering the confirm password")
        self.rp.submit_button()
        self.log.info("clicking submit button")
        self.log.info("saving customer info")
        self.log.info("user_registration validation start")
        self.msg = self.driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml("
                                                      "message.text)']").text
        if 'Thank you for registering with Main Website Store.' in self.msg:
            assert True == True
            self.driver.save_screenshot(".\\Screenshot\\test_registration_001_pass.png")
            self.log.info("test_registration_001 is pass")
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_registration_001_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_registration_001",
                          attachment_type=AttachmentType.PNG)
            self.log.info("test_registration_001 is fail")
            assert True == False

        self.driver.close()
        self.log.info("Ending of test_registration_001")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# driver.find_element(By.LINK_TEXT, "Create an Account").click()
# driver.find_element(By.ID,"firstname").send_keys("Lukesh")
# driver.find_element(By.ID,"lastname").send_keys("Ade")
# # driver.find_element(By.NAME,"is_subscribed").click()
# driver.find_element(By.NAME,"email").send_keys("lukeshade@gmail.com")
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test@123")
# driver.find_element(By.ID,"password-confirmation").send_keys("Test@123")
# driver.find_element(By.XPATH,"//button[@class='action submit primary']").click()
# driver.close()
