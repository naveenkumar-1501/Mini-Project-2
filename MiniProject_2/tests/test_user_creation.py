"""
test_user_creation.py
Tests the creation of a new user.
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from MiniProject_2.pages.login_page import LoginPage
from MiniProject_2.pages.pim_page import PimPage
from MiniProject_2.common import Config

@pytest.mark.usefixtures("driver")
class TestUserCreation:
    def test_create_new_user(self, driver):
        print("Navigating to login page...")
        driver.get(Config.URL)
        # Debugging: Print current URL
        print("Current URL:", driver.current_url)
        # Ensure the login page is fully loaded
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Config.PAGE_INDICATOR)))
        login_page = LoginPage(driver)
        # Login as Admin
        login_page.login("Admin", "admin123")
        # Wait for Pim button to be clickable and click
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Config.PIM_BUTTON))).click()
        pim_page = PimPage(driver)
        # Click 'Add User'
        pim_page.click_add_user()
        # Fill in employee details
        first_name = "Naveen"
        middle_name = "Kumar"
        last_name = "K"
        pim_page.fill_employee_name(first_name, middle_name, last_name)
        # Fill in employee ID
        employee_id = "1501"
        pim_page.fill_employee_id(employee_id)
        # Toggle 'Create Login Details'
        pim_page.toggle_create_login_details()
        # Fill in login details
        username = "Naveen"
        password = "naveen@123"
        pim_page.fill_login_details(username, password)
        # Save the new user
        pim_page.save_user()
        print("Save button clicked and user details submitted.")
        # Logout Admin
        print("Logging out Admin...")
        login_page.logout()
        # Debugging: Verify redirection to login page
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Config.PAGE_INDICATOR)))
        print("Redirected to login page.")
        # Login with the new user credentials
        print("Logging in with the new user credentials...")
        login_page.login(username, password)
        # Validate login for the new user
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Config.DASHBOARD_BUTTON)))
            print(f"New user '{username}' successfully logged in.")
        except Exception as e:
            print(f"Login failed for new user '{username}'. Error: {e}")
            pytest.fail(f"New user '{username}' could not log in.")
