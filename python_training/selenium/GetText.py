
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.saucedemo.com/"

driver.get(url)
user= driver.find_element(By.ID,"user-name")

user.click()
user.send_keys("standard_user")
pw = driver.find_element(By.ID,"password")
pw.send_keys("secret_sauce")
login_button = driver.find_element(By.ID,"login-button")
login_button.click()

price = driver.find_element(By.CLASS_NAME,"inventory_item_price")
price_text = price.text
print (f"Price found the value is {price_text}")
list_of_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

for element in list_of_elements:
    price_text_from_list = element.text
    print (f"the price is {price_text_from_list}")

driver.close()
print ("Test end ")

