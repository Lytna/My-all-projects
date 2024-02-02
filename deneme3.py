from selenium import webdriver
from time import sleep  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
sleep(6)
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR, '[id="user-message"]').send_keys("Selenium deneme 1-2-3")
sleep(1)
driver.find_element(By.CSS_SELECTOR, '[id="showInput"]').click()

girilenmetin = driver.find_element(By.CSS_SELECTOR, '[id="message"]').text
sleep(1)
print("Sisteme girilen metin:",girilenmetin)

driver.find_element(By.CSS_SELECTOR, '[id="sum1"]').send_keys(5)
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[id="sum2"]').send_keys(10)
driver.find_element(By.CSS_SELECTOR, '[id="gettotal"] [type="button"]').click()


sleep(300)