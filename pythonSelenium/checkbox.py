import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#https://rahulshettyacademy.com/AutomationPractice/
service_Obj=  Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for a in checkboxes:
    if a.get_attribute("value")== "option2":
        a.click()
        assert a.is_selected()
        break
time.sleep(3)

radiobuttons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break
time.sleep(3)

