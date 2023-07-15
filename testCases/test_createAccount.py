import string
from random import random
from pageObject.UserAccount_Page import UserRegistrationClass

from utilities.ReadConfigFile import ReadConfig


class Test_CreateAccount:
    url = ReadConfig.get_application_url()
    password = ReadConfig.get_password()

    def test_registration_001(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.rp = UserRegistrationClass(self.driver)
        self.rp.link_registration()
        self.rp.firstname("Lukesh")
        self.rp.lastname("Ade")
        self.email = random_generator() + "@gmail.com"
        self.rp.email(self.email)
        self.rp.password(self.password)
        self.rp.confirm_password(self.password)
        self.rp.submit_button()


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
