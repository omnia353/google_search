from test_cases.base_tests import BaseTest
import time


class CheckButtonText(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url()

    def test01_btn(self):
        """
        TEST01: Check whether first link in google search is what i'm search for.
            1- Write http://google.com
            2- Write coursera in google search bar
            3- Navigate through fist link of results
            4- Verify existance of join for free button
        """
        self.search_page.search_for_word(self.base_selenium.txt_3)
        self.base_selenium.click(element='search:first_link')
        btn_txt = self.coursera_home_page.get_btn_txt()
        self.base_selenium.LOGGER.info('There is join for free button.')
        self.assertEqual("Join for Free", btn_txt)
