from selenium import webdriver
from selenium.webdriver.common.by import By


class UserLoginClass:

    linkUserLogin_XPATH = (By.XPATH, "//div[@class='panel header']//li[@data-label='or']")
    # driver.find_element(By.XPATH, "//div[@class='panel header']//li[@data-label='or']").click()
    textBoxEmail_ID = (By.ID, "email")
    # driver.find_element(By.ID, "email").send_keys("lukeshade@gmail.com")
    textBoxPassword_ID = (By.ID, "pass")
    # driver.find_element(By.ID, "pass").send_keys("Test@123")
    buttonSignin_ID = (By.ID, "send2")
    # driver.find_element(By.ID, "send2").click()

    def __init__(self, driver):
        self.driver = driver

    def link_userlogin(self):
        self.driver.find_element(*UserLoginClass.linkUserLogin_XPATH).click()

    def email(self, email):
        self.driver.find_element(*UserLoginClass.textBoxEmail_ID).send_keys(email)

    def password(self, password):
        self.driver.find_element(*UserLoginClass.textBoxPassword_ID).send_keys(password)

    def signin_button(self):
        self.driver.find_element(*UserLoginClass.buttonSignin_ID).click()
