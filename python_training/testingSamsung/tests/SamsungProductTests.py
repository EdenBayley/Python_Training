import unittest

from selenium.webdriver.common.by import By

from python_training.testingSamsung.pages.HomePage import HomePage
from python_training.testingSamsung.pages.SearchResults import SearchResults
from python_training.testingSamsung.tests.globalSamsung import urlSamsung
from python_training.testingSamsung.tests.samsungSelenium import samsungSelenium


class SamsungProductTests(unittest.TestCase):

    def setUp(self):
        base = samsungSelenium()
        self.driver = base.selenium_start(urlSamsung)
        home_page = HomePage(self.driver)
        home_page.search_Function()
        self.search_results = SearchResults(self.driver)
        self.test_product_successful_search()
        self.test_product_name()

    def test_product_successful_search(self):
        self.search_results.get_search_results_bar()

    def test_product_name(self):
        self.search_results.get_product_title()

    def test_product_price(self):
        self.search_results.get_product_price()

    if __name__ == "__main":
        unittest.main()


        print("Test End")
