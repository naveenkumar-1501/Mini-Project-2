"""
pim_page.py
Page Object for PIM (Personal Information Management) functionality.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from MiniProject_2.common import Config
from MiniProject_2.pages.base_page import BasePage

class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)
        self.add_user_button = (By.XPATH, Config.ADD_BUTTON)
        self.employee_name_field = (By.XPATH, Config.EMPLOYEE_NAME)
        self.search_button = (By.XPATH, Config.SEARCH_BUTTON)

    def click_add_user(self):
        """Clicks the 'Add' button to add a new user."""
        self.wait_for_element(self.add_user_button, condition='clickable').click()

    def fill_employee_name(self, first_name, middle_name, last_name):
        """Fills the first name, middle name, and last name fields."""
        first_name_input = self.wait_for_element((By.XPATH, Config.FIRST_NAME), condition='presence')
        first_name_input.send_keys(first_name)
        middle_name_input = self.wait_for_element((By.XPATH, Config.MIDDLE_NAME), condition='presence')
        middle_name_input.send_keys(middle_name)
        last_name_input = self.wait_for_element((By.XPATH, Config.LAST_NAME), condition='presence')
        last_name_input.send_keys(last_name)

    def fill_employee_id(self, employee_id):
        """Clears and fills the employee ID field."""
        employee_id_input =self.wait_for_element((By.XPATH, Config.EMPLOYEE_ID), condition='presence')
        employee_id_input.click()
        employee_id_input.send_keys(Keys.CONTROL + "a")
        employee_id_input.send_keys(Keys.BACKSPACE)
        employee_id_input.send_keys(employee_id)

    def toggle_create_login_details(self):
        """Toggles the 'Create Login Details' switch."""
        self.wait_for_element((By.XPATH, Config.TOGGLE_BUTTON), condition='clickable').click()

    def fill_login_details(self, username, password):
        """Fills the username, password, and confirm password fields."""
        user_name_input = self.wait_for_element((By.XPATH, Config.NEW_USERNAME_FIELD), condition='presence')
        user_name_input.send_keys(username)
        password_input = self.wait_for_element((By.XPATH, Config.NEW_PASSWORD_FIELD), condition='presence')
        password_input.clear()
        password_input.send_keys(password)
        confirm_password_input = self.wait_for_element((By.XPATH, Config.CONFIRM_PASSWORD_FIELD), condition='presence')
        confirm_password_input.send_keys(password)

    def save_user(self):
        """Clicks the Save button to save the user details."""
        save_button = self.wait_for_element((By.XPATH, Config.SAVE_BUTTON), condition='clickable')
        if save_button.is_enabled():
            save_button.click()
        else:
            print("Save button is not enabled.")
        success_message = self.wait_for_element((By.XPATH, Config.SUCCESS_MESSAGE), condition='presence')
        print("Success Message:", success_message.text)

    def search_employee_by_name(self, employee_name):
        """Searches for an employee by name in the PIM section."""
        # Enter the employee name in the search field
        employee_name_input = self.wait_for_element(self.employee_name_field, condition='presence')
        employee_name_input.clear()
        employee_name_input.send_keys(employee_name)
        search_button = self.wait_for_element(self.search_button, condition='clickable')
        search_button.click()

    def verify_employee_record_exists(self, employee_name):
        """Verifies if the employee record exists in the search results."""
        from selenium.webdriver.common.by import By  # local import
        employee_record = (By.XPATH, Config.RECORD)
        try:
            self.wait_for_element(employee_record, condition='presence')
            return True
        except Exception as error:
            print(f"Error verifying employee record '{employee_name}': {error}")
            return False
