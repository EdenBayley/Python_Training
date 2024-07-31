# homework -
# https://demo.guru99.com/test/newtours/reservation.php
# לעשות באתר הזמנה שלמה ולשלוח אותה
import time
from telnetlib import EC
from time import sleep

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from python_training.selenium.SeleniumBaseExampleTwo import SeleniumBase

selenium_base = SeleniumBase()

driver = selenium_base.selenium_start("https://demo.guru99.com/test/newtours/reservation.php")
sleep(5)

dropdown_element = driver.find_element(By.NAME, "passCount")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("2")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "fromPort")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("London")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "fromMonth")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("August")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "fromDay")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("9")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "toPort")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("New York")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "toMonth")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("November")

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "toDay")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("9")


wait = WebDriverWait(driver, 10)

check_box = driver.find_elements(By.CLASS_NAME, "servClass")
check_box[0].click()

time.sleep(2)

dropdown_element = driver.find_element(By.NAME, "airline")
select_dropdown = Select(dropdown_element)
select_dropdown.select_by_visible_text("Unified Airlines")

time.sleep(2)

con = driver.find_element(By.LINK_TEXT,"CONTINUE")
con.click()




driver.quit()




