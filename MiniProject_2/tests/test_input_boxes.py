"""
test_input_boxes.py
Validates the visibility of input boxes on the login page.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject_2.common import Config

class TestInputBoxes:
    """Test cases to validate the visibility of input boxes on the login page."""
    @pytest.mark.usefixtures("driver")
    def test_username_input_visible(self, driver):
        """Verifies the username input box is visible on the page."""
        driver.get(Config.URL)
        # Wait for the username input to be present and visible
        try:
            username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Config.USER_NAME_FIELD)))
            assert username_input.is_displayed(), "Username input box is not visible"
        except Exception as error:
            print("Error:", error)
            raise AssertionError("Username input box not found or visible.")
    @pytest.mark.usefixtures("driver")
    def test_password_input_visible(self, driver):
        """Verifies the password input box is visible on the page."""
        driver.get(Config.URL)
        # Wait for the password input to be present and visible
        try:
            password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Config.PASSWORD_FIELD)))
            assert password_input.is_displayed(), "Password input box is not visible"
        except Exception as error:
            print("Error:", error)
            raise AssertionError("Password input box not found or visible.")