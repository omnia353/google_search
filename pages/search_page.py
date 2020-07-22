from pages.base_page import BasePage


class SearchPage(BasePage):
    def search_for_word(self, word):
        self.base_selenium.LOGGER.info('search for {} in google.'.format(word))
        self.base_selenium.write(element='search:search_bar', txt=word)
        self.base_selenium.submit(element='search:search_bar')

    def get_first_link(self, word):
        self.base_selenium.LOGGER.info('get the first link.')
        return self.base_selenium.get_text(element='search:first_link')
