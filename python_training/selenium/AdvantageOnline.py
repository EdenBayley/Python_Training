from time import sleep

from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExampleTwo import SeleniumBase

selenium_base = SeleniumBase()
driver = selenium_base.selenium_start("https://advantageonlineshopping.com/#/")
sleep(5)
contact = driver.find_element(By.LINK_TEXT,"CONTACT US")
contact.click()

sort_category = select(driver.select_element(By.NAME,"productListboxContactUs"))
sort_category.select_by_visible_text("Laptops")

sort_product = select(driver.select_element(By.NAME,"productListboxContactUs"))
sort_product.select_by_value("HP Chromebook 14 G1 (ES)")

contact = driver.find_element(By.LINK_TEXT,"CONTACT US")
contact.click()



selenium_base.selenium_end(driver)






