import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#https://rahulshettyacademy.com/AutomationPractice/
service_Obj=  Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
dropdown_input= driver.find_element(By.ID, "autocomplete")
dropdown_input.send_keys("ind")

time.sleep(3)
countries= driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

assert dropdown_input.get_attribute("value") == "India"