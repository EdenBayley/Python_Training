import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Keys


class SeleniumBase():
    def selenium_start(self, url):
        print("test start")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(url)
        return driver


    def selenium_end(self,driver):
        driver.close()
        print("test end")