from selenium import webdriver
from time import sleep  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
driver.implicitly_wait(30)

sleep(5)
driver.find_element(By.CSS_SELECTOR, '[id="isAgeSelected"]').click()
sleep(1.5)
driver.find_element(By.CSS_SELECTOR, '[value="Check All"]').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[value="Uncheck All"]').click()
sleep(0.8)
driver.find_element(By.CSS_SELECTOR, '[id="ex1-check1"]').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[id="ex1-check2"]').click()
sleep(0.5)
checkboxes = driver.find_elements(By.CSS_SELECTOR, '[class="cb-element mr-10" ]')

i = 0
for n in checkboxes:    
    if i == 3:
        n.click()
    i+=1


sleep(300)