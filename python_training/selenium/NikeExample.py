from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.nike.com"

driver.get(url)
men_button = driver.find_element(By.LINK_TEXT, "Men")
men_button.click()

driver.close()
print("test end")