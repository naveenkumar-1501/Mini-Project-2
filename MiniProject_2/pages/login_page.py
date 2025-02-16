"""
login_page.py
Page Object for login functionality.
"""

from selenium.webdriver.common.by import By
from MiniProject_2.common import Config
from MiniProject_2.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)
        self.username_input = (By.XPATH, Config.USER_NAME_FIELD)
        self.password_input = (By.XPATH, Config.PASSWORD_FIELD)
        self.login_button = (By.XPATH, Config.LOGIN_BUTTON)
        self.logout_button = (By.XPATH, Config.LOGOUT_BUTTON)
        self.page_indicator = (By.XPATH, Config.PAGE_INDICATOR)
        self.dropdown_button = (By.XPATH, Config.DROP_DOWN_BUTTON)

    def login(self, username, password):
        """Logs in using the provided username and password."""
        try:
            # Wait for a unique element on the login page
            self.wait_for_element(self.page_indicator, condition='presence')
            # Enter username and password, then click login
            self.wait_for_element(self.username_input, condition='visible').send_keys(username)
            self.wait_for_element(self.password_input, condition='visible').send_keys(password)
            self.wait_for_element(self.login_button, condition='clickable').click()
        except Exception as error:
            print(f"Error occurred during login: {error}")
            raise

    def logout(self):
        """Logs out of the application."""
        try:
            self.wait_for_element(self.dropdown_button, condition='clickable').click()
            self.wait_for_element(self.logout_button,  condition='clickable').click()
            print("Logout successful.")
        except Exception as error:
            print(f"Error occurred during logout: {error}")
            raise
