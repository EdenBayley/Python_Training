
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("test start")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com")
search = driver.find_element(By.ID,"APjFqb")
search.click()
search.click()
search.send_keys("CAT")
search.send_keys(Keys.ENTER)


driver.close()
print ("test end")