import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#https://rahulshettyacademy.com/AutomationPractice/
service_Obj=  Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Deepti")
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
assert "Deepti" in alert.text
alert.accept()
time.sleep(3)