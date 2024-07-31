from selenium.webdriver.common.by import By

from python_training.selenium.SeleniumBaseExample import SeleniumBaseExample


class cssExample():
  base = SeleniumBaseExample()
  driver = base.selenium_start("https://www.saucedemo.com/")
  user = driver.find_element(By.CSS_SELECTOR,"input[class='input_error form_input']")
  user.click()
  user.send_keys("standard_user")
  #pw = driver.find_element(By.CSS_SELECTOR,"input[data-test='password']")

  elemnts = driver.find_elements(By.CSS_SELECTOR,"input[class='input_error form_input']")
  pw = elemnts[1]
  pw.click()
  pw.send_keys("secret_sauce")
  login = driver.find_element(By.CSS_SELECTOR,"input[class='submit-button btn_action']")
  login.click()



  base.selenium_end(driver)