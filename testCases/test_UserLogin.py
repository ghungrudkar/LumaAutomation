import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='panel header']//li[@data-label='or']").click()
driver.find_element(By.ID,"email").send_keys("lukeshade@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Test@123")
driver.find_element(By.ID,"send2").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "div[class='panel header'] button[type='button']").click()
driver.find_element(By.XPATH,"//div[@aria-hidden='false']//li[@data-label='or']").click()
driver.close()
