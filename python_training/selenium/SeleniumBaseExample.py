
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumBaseExample():

    def selenium_start(self,url):
        print ("test start")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium_end(self,driver):
        driver.close()
        print ("test end")