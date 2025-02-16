"""
test_home_url.py
Verifies the home URL.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject_2.common import Config

class TestHomeURL:
    """Tests for verifying the home URL."""
    @pytest.mark.usefixtures("driver")
    def test_home_url(self, driver):
        """Verifies that the home URL matches the expected URL."""
        # Navigate to the home page explicitly
        driver.get(Config.URL)
        # Define the expected URL
        expected_url = Config.URL
        try:
            # Wait for the page to load (use a reliable locator like the login form container)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='orangehrm-login-container']")))
            # Get the actual URL
            actual_url = driver.current_url
            # Assert the URLs match
            assert actual_url == expected_url, f"Expected URL: {expected_url}, but got {actual_url}"
            print(f"Test passed: Home URL is {actual_url}, as expected.")
        except Exception as error:
            # Log debug information on failure
            print("Page source for debugging:", driver.page_source)
            raise AssertionError(f"Test failed due to: {error}")
