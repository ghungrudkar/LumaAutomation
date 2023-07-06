from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.UserAccount_Page import UserRegistrationClass


class Test_CreateAccount:
    def test_registration_001(self, setup):
        self.driver = setup
        self.rp = UserRegistrationClass(self.driver)
        self.rp.link_registration()
        self.rp.firstname("Lukesh")
        self.rp.lastname("Ade")
        self.rp.email(self.rp.generate_random_username() + "@gmail.com")
        self.rp.password("Test@123")
        self.rp.confirm_password("Test@123")
        self.rp.submit_button()

# driver.find_element(By.LINK_TEXT, "Create an Account").click()
# driver.find_element(By.ID,"firstname").send_keys("Lukesh")
# driver.find_element(By.ID,"lastname").send_keys("Ade")
# # driver.find_element(By.NAME,"is_subscribed").click()
# driver.find_element(By.NAME,"email").send_keys("lukeshade@gmail.com")
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test@123")
# driver.find_element(By.ID,"password-confirmation").send_keys("Test@123")
# driver.find_element(By.XPATH,"//button[@class='action submit primary']").click()
# driver.close()
