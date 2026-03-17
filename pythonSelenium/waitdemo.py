import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#https://rahulshettyacademy.com/AutomationPractice/
service_Obj=  Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
produces = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(produces)
print(count)

for produce in produces:
    produce.find_element(By.XPATH,"div/button").click()
time.sleep(5)
