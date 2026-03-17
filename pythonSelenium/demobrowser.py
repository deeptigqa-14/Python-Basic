import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver service helps in opening the browser .
service_obj = Service("c:/Users/deept/Documents/Drivers/chromedriver.exe") # if internet is not allowed then we have to download the driver manually and provide the path of the driver in the below line
# https://googlechromelabs.github.io/chrome-for-testing/ ( download from here and provide the path in Service()
driver = webdriver.Chrome(service=service_obj) # this line opens the browser
#driver = webdriver.Chrome() # checks the chrome version and search the deriver on internet and download it automatically4
#driver = webdriver.Firefox() # for firefox gecko driver
#driver = webdriver.Edge() # for edge

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)


