from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExample import SeleniumBaseExample


class cssExample():
  base = SeleniumBaseExample()
  driver = base.selenium_start("https://demo.applitools.com/app.html")
  search = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Start typing to search...']")
  search.click()
  search.send_keys("hello")


  base.selenium_end(driver)