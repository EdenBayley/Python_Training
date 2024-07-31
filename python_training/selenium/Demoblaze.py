# Go to https://www.demoblaze.com/
# 2. Make sure the text over contact is “Contacts”
# 3. Click on it if the text is as expected

#https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

#click on Bank Manager Login

#Bank Assignment:

from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

list_of_elements = driver.find_elements(By.CLASS_NAME, "btn.btn-primary.btn-lg")

list_of_elements[1].click()

selenium_base.selenium_end(driver)