from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
# search = driver.find_element(By.ID,"APjFqb")
# search.click()
# search.click()
# search.send_keys("Cat")
# search.send_keys(Keys.ENTER)

driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.click()
password.send_keys("secret_sauce")
login_key = driver.find_element(By.ID,"login-button")
login_key.click()

driver.maximize_window()
driver.close()
print("Test end")