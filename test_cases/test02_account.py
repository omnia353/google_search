from test_cases.base_tests import BaseTest


class CreateAccount(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url()

    def test01_signup_with_used_acc(self):
        """
        TEST01: Check whether first link in google search is what i'm search for.
            1- Write http://google.com
            2- Write leetcode in google search bar
            3- Navigate through fist link of results
            4- Click sign up btn
            5- Fill form with an existing username
            6- Verify that page url doesn't change
        """
        self.search_page.search_for_word(self.base_selenium.txt_2)
        self.base_selenium.click(element='search:first_link')
        self.base_selenium.click(element='account:btn')
        url1 = self.base_selenium.get_current_url()
        self.create_account.fill_form()
        url2 = self.base_selenium.get_current_url()
        self.base_selenium.LOGGER.info('fail to login.')
        self.assertEqual(url1, url2)
