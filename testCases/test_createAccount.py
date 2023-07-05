from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Create an Account").click()
driver.find_element(By.ID,"firstname").send_keys("Lukesh")
driver.find_element(By.ID,"lastname").send_keys("Ade")
# driver.find_element(By.NAME,"is_subscribed").click()
driver.find_element(By.NAME,"email").send_keys("lukeshade@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test@123")
driver.find_element(By.ID,"password-confirmation").send_keys("Test@123")
driver.find_element(By.XPATH,"//button[@class='action submit primary']").click()

