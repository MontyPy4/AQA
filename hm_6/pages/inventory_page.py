from selenium.webdriver.common.by import By

from hm_6.pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.click(self.BACKPACK_BUTTON)
        self.click(self.TSHIRT_BUTTON)
        self.click(self.ONESIE_BUTTON)

    def open_cart(self):
        self.click(self.CART_BUTTON)