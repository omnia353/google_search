from unittest import TestCase
from framework.base_selenium import BaseSelenium
from pages.search_page import SearchPage
from pages.create_account import CreateAcc
from pages.coursera_home_page import HomePage


class BaseTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_selenium = BaseSelenium()
        self.search_page = SearchPage()
        self.create_account = CreateAcc()
        self.coursera_home_page = HomePage()

    def setUp(self):
        self.base_selenium.get_driver()

    def tearDown(self):
        self.base_selenium.quit_driver()
