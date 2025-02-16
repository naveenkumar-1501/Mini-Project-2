"""
base_page.py
Centralizes common wait functionality for page objects.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator, condition='visible'):
        """Waits for an element based on the given condition.
        Args:
            locator (tuple): Locator tuple (By, value).
            condition (str): 'visible', 'clickable', or 'presence'.
        Returns:
            WebElement after the condition is met.
        """
        if condition == 'visible':
            return self.wait.until(EC.visibility_of_element_located(locator))
        elif condition == 'clickable':
            return self.wait.until(EC.element_to_be_clickable(locator))
        elif condition == 'presence':
            return self.wait.until(EC.presence_of_element_located(locator))
        else:
            raise ValueError(f"Unknown condition: {condition}")
