import unittest

from python_training.selenium_page_object.Pages.LoginPage import loginPage
from python_training.selenium_page_object.Pages.ProductPage import productPage
from python_training.selenium_page_object.Tests.baseSelenium import baseSelenium
from python_training.selenium_page_object.Tests.globals import url_base, user_text, pw_text


class test_price_text(unittest.TestCase):

    def test_first_price_text(self):

        base = baseSelenium()


        driver = base.selenium_start(url_base)
        login_page = loginPage(driver)
        product_page = productPage(driver)

        login_page.login_with_user_pw(user_text,pw_text)
        price_text = product_page.get_product_price()


        base.selenium_end(driver)

