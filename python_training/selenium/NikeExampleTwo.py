from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()

driver = selenium_base.selenium_start("https://www.nike.com")

men_button = driver.find_element(By.LINK_TEXT, "Men")
men_button.click()

selenium_base.selenium_end(driver)


