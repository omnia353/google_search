from pages.base_page import BasePage


class CreateAcc(BasePage):

    def fill_form(self):
        self.base_selenium.LOGGER.info('Fill in login form.')
        self.base_selenium.write(element='account:ip_user_name', txt=self.base_selenium.username)
        self.base_selenium.write(element='account:ip-password', txt=self.base_selenium.password)
        self.base_selenium.write(element='account:ip-confirm', txt=self.base_selenium.password)
        self.base_selenium.write(element='account:ip-email', txt=self.base_selenium.email)
        self.base_selenium.click(element='account:signup_btn')
