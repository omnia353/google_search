from test_cases.base_tests import BaseTest


class TextSearch(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url()

    def test01_check_first_link(self):
        """
        TEST01: Check whether first link in google search is what i'm search for.
            1- Enter http://google.com
            2- Write instagram in google search bar
            3- click submit
            4- Verify that first link contain 'instagram' text
        """
        self.search_page.search_for_word(self.base_selenium.txt_1)
        text = self.search_page.get_first_link(self.base_selenium.txt_1)
        self.base_selenium.LOGGER.info('the first link contain instagram word.')
        self.assertIn(self.base_selenium.txt_1,text.lower())


