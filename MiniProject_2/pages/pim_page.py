"""
pim_page.py
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject_2.common import Config

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_user_button = (By.XPATH, Config.ADD_BUTTON)
        self.employee_name_field = (By.XPATH, Config.EMPLOYEE_NAME)
        self.search_button = (By.XPATH, Config.SEARCH_BUTTON)

    def click_add_user(self):
        """Clicks the 'Add' button to add a new user."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_user_button)).click()

    def fill_employee_name(self, first_name, middle_name, last_name):
        """Fills the first name, middle name, and last name fields."""
        first_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.FIRST_NAME)))
        first_name_input.send_keys(first_name)
        middle_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.MIDDLE_NAME)))
        middle_name_input.send_keys(middle_name)
        last_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.LAST_NAME)))
        last_name_input.send_keys(last_name)

    def fill_employee_id(self, employee_id):
        """Clears and fills the employee ID field."""
        employee_id_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.EMPLOYEE_ID)))
        employee_id_input.click()
        employee_id_input.send_keys(Keys.CONTROL + "a")
        employee_id_input.send_keys(Keys.BACKSPACE)
        employee_id_input.send_keys(employee_id)

    def toggle_create_login_details(self):
        """Toggles the 'Create Login Details' switch."""
        toggle_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.TOGGLE_BUTTON)))
        toggle_button.click()

    def fill_login_details(self, username, password):
        """Fills the username, password, and confirm password fields."""
        user_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.NEW_USERNAME_FIELD)))
        user_name_input.send_keys(username)
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.NEW_PASSWORD_FIELD)))
        password_input.clear()
        password_input.send_keys(password)
        confirm_password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.CONFIRM_PASSWORD_FIELD)))
        confirm_password_input.send_keys(password)

    def save_user(self):
        """Clicks the Save button to save the user details."""
        save_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Config.SAVE_BUTTON)))
        if save_button.is_enabled():
            save_button.click()
        else:
            print("Save button is not enabled.")
        success_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Config.SUCCESS_MESSAGE)))
        print("Success Message:", success_message.text)

    def search_employee_by_name(self, employee_name):
        """Searches for an employee by name in the PIM section."""
        # Enter the employee name in the search field
        employee_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.employee_name_field))
        employee_name_input.clear()
        employee_name_input.send_keys(employee_name)
        # Click the search button
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button))
        search_button.click()

    def verify_employee_record_exists(self, employee_name):
        """Verifies if the employee record exists in the search results."""
        employee_record = (By.XPATH, Config.RECORD)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(employee_record))
            return True
        except Exception as error:
            print(f"Error verifying employee record '{employee_name}': {error}")
            return False
