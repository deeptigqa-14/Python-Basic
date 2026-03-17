import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("c:/Users/deept/Documents/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

email = driver.find_element(By.NAME,"email")
email.send_keys("test@test.com")
password = driver.find_element(By.ID,"exampleInputPassword1")
password.send_keys("12345")
check = driver.find_element(By.ID,"exampleCheck1")
check.click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

radio = driver.find_element(By.ID,"inlineRadio1")
submitBtn = driver.find_element(By.XPATH,"//input[@type='submit']") #find element with xpath with indexing
# css_selector can be constructed , #id value can be used  or .classname
submitBtn.click()
name = driver.find_element(By.CSS_SELECTOR , "input[name='name']")
name.send_keys("test")

msg = driver.find_element(By.CLASS_NAME,'alert-success').text

#ssert msg == "Success"
print(msg)
assert "Success" in msg

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Deepti")

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(5)