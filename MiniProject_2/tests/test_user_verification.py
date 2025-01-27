"""
test_user_verification.py
"""
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from MiniProject_2.pages.login_page import LoginPage
from MiniProject_2.pages.pim_page import PimPage
from MiniProject_2.common import Config

class TestUserVerification:
    def test_user_verification(self, driver):
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
        # Search for the user by name
        employee_name = "Naveen"
        pim_page.search_employee_by_name(employee_name)
        # Verify if the user record exists
        assert pim_page.verify_employee_record_exists(employee_name), f"Employee '{employee_name}' not found in the records."