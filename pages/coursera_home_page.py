from pages.base_page import BasePage


class HomePage(BasePage):
    def get_btn_txt(self):
        return self.base_selenium.get_text(element='homepage:btn')
