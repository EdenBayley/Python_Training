# https://www.calculator.net/password-generator.html
import time

from selenium.webdriver.common.by import By

#from python_training.selenium import seleniumBaseExample
#from python_training.selenium.seleniumBaseExample import seleniumBaseExample

from python_training.selenium.SeleniumBaseExampleTwo import SeleniumBase

selenium_base = SeleniumBase()

driver = selenium_base.selenium_start("https://www.calculator.net/password-generator.html")

check_box = driver.find_elements(By.CLASS_NAME, "cbmark")
check_box[0].click()
check_box[1].click()
check_box[2].click()
check_box[3].click()
check_box[4].click()
check_box[5].click()

check_box[1].click()
check_box[2].click()
check_box[3].click()

submit = driver.find_element(By.NAME, "submit1")
submit.click()
time.sleep(5)
result = driver.find_element(By.ID, "resultid")
pw = result.text
start_index = pw.index("Password")+9
stop_index = pw.index("Password Strength")-1
final = pw[start_index:stop_index]
final.strip()


print(f'the result is {final}')

selenium_base.selenium_end(driver)

# homework -
# https://demo.guru99.com/test/newtours/reservation.php
# לעשות באתר הזמנה שלמה ולשלוח אותה