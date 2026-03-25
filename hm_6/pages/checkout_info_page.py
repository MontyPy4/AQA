from selenium.webdriver.common.by import By

from hm_6.pages.base_page import BasePage

class CheckoutInfoPage(BasePage):
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIPCODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def checkout_info(self, firstname, lastname, zipcode):
        self.input(self.FIRSTNAME_INPUT, firstname)
        self.input(self.LASTNAME_INPUT, lastname)
        self.input(self.ZIPCODE_INPUT, zipcode)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)


