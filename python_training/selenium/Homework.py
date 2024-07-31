# https://www.egged.co.il/HomePage.aspx
# https://demoqa.com/login


# 1.
# Go to - https://www.egged.co.il/HomePage.aspx
# Set to and from details.

import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

print ("start test")

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.egged.co.il/HomePage.aspx")

From_input = driver.find_element(By.ID, "From")
From_input.click()
From_input.send_keys("jerusalem")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-1 li")))
From_input.send_keys(Keys.ENTER)

To_input = driver.find_element(By.ID,"To")
To_input.click()
To_input.send_keys("Rishon LeZion")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-1 li")))
To_input.send_keys(Keys.ENTER)

get_directions_button = driver.find_element(By.ID,"get_directions-button")
get_directions_button.click()

driver.maximize_window()

driver.quit()

print("end test")




