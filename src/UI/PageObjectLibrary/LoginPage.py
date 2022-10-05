from selenium.webdriver.common.by import By
from src.UI.PageObjectLibrary.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        self.do_send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    def click_login_button(self):
        self.do_click(self.LOGIN_BUTTON)
