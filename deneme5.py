from selenium import webdriver
from time import sleep  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
driver.implicitly_wait(30)
sleep(5)
driver.find_element(By.CSS_SELECTOR, '[value="Female"]').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[id="buttoncheck"]').click()
sleep(0.5)
response = driver.find_element(By.CSS_SELECTOR, '[class="text-gray-900 text-size-15 my-10 text-black radiobutton"]').text
print(response)
sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '[class="text-size-16 mt-10 text-black mr-20"] [value="Female"]').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[value="5 - 15"]').click()
sleep(0.5)
buttons = driver.find_elements(By.CSS_SELECTOR, '[type="button"]')

for n in buttons:
    if n.text == "Get values":
        n.click()

response = driver.find_element(By.CSS_SELECTOR, '[class="w-4/12 smtablet:w-full rigth-input"]').get_attribute("textContent")
print(response)

sleep(300)