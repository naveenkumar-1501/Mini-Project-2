"""
login_page.py
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from MiniProject_2.common import Config

class LoginPage:
      def __init__(self, driver):
          self.driver = driver
          self.username_input = (By.XPATH, Config.USER_NAME_FIELD)
          self.password_input = (By.XPATH, Config.PASSWORD_FIELD)
          self.login_button = (By.XPATH, Config.LOGIN_BUTTON)
          self.logout_button = (By.XPATH, Config.LOGOUT_BUTTON)

      def login(self, username, password):
          """
          Logs in using the provided username and password.
          Args: username (str): The username to log in.
          password (str): The password to log in.
          """
          try:
              WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.PAGE_INDICATOR)))
              # Enter the username
              WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
              # Enter the password
              WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
              # Click the login button
              WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
          except Exception as error:
              print(f"Error occurred during login: {error}")
              raise

      def logout(self):
          """Logs out of the application."""
          try:
              # Locate and click the profile dropdown
              WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.DROP_DOWN_BUTTON))).click()
              # Locate and click the logout button
              WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.LOGOUT_BUTTON))).click()
              print("Logout successful.")
          except Exception as error:
              print(f"Error occurred during logout: {error}")
              raise
