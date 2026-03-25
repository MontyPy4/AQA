from selenium.webdriver.common.by import By

from hm_6.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open_page(self,driver):
        driver.get(self.URL)

    def login(self, username, password):
        self.input(self.USERNAME_INPUT, username)
        self.input(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

