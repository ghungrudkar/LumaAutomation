import string
from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By


class UserRegistrationClass:

    linkCreateAccount_LINK_TEXT = (By.LINK_TEXT, "Create an Account")
    # driver.find_element(By.LINK_TEXT, "Create an Account").click()
    textBoxFirstname_ID = (By.ID, "firstname")
    # driver.find_element(By.ID, "firstname").send_keys("Lukesh")
    textBoxLastname_ID = (By.ID, "lastname")
    # driver.find_element(By.ID, "lastname").send_keys("Ade")
    textBoxEmail_NAME = (By.NAME, "email")
    # driver.find_element(By.NAME, "email").send_keys("lukeshade@gmail.com")
    textBoxPassword_XPATH = (By.XPATH, "//input[@id='password']")
    # driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Test@123")
    textBoxConfirmPassword_ID = (By.ID, "password-confirmation")
    # driver.find_element(By.ID, "password-confirmation").send_keys("Test@123")
    buttonSubmit_XPATH = (By.XPATH, "//button[@class='action submit primary']")
    # driver.find_element(By.XPATH, "//button[@class='action submit primary']").click()

    def __init__(self, driver):
        self.driver = driver

    def link_registration(self):
        self.driver.find_element(*UserRegistrationClass.linkCreateAccount_LINK_TEXT).click()

    def firstname(self, firstname):
        self.driver.find_element(*UserRegistrationClass.textBoxFirstname_ID).send_keys(firstname)

    def lastname(self, lastname):
        self.driver.find_element(*UserRegistrationClass.textBoxLastname_ID).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(*UserRegistrationClass.textBoxEmail_NAME).send_keys(email)

    def password(self, password):
        self.driver.find_element(*UserRegistrationClass.textBoxPassword_XPATH).send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element(*UserRegistrationClass.textBoxConfirmPassword_ID).send_keys(confirm_password)

    def submit_button(self):
        self.driver.find_element(*UserRegistrationClass.buttonSubmit_XPATH).click()

    # def generate_random_username(self):
    #     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
