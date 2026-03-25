from selenium.webdriver.common.by import By

from hm_6.pages.base_page import BasePage


class CheckoutTotalPage(BasePage):

    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def get_total_price(self):
        total_price = self.get_text(self.TOTAL_PRICE)
        return float(total_price.replace("Total: $", ""))