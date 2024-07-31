from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.calculator.net/")
elements_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Calculator")
num_of_elements = len(elements_link)
print(f"{num_of_elements}")

selenium_base.selenium_end(driver)