import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

#driver.find_element(By.LINK_TEXT,"Forgot password?").clear()
driver.find_element(By.PARTIAL_LINK_TEXT,"password?").click()

driver.find_element(By.XPATH,"//form/Div[1]/input").send_keys("Demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("12345")
driver.find_element(By.XPATH,"//form/div[3]/input").send_keys("12345")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(5)