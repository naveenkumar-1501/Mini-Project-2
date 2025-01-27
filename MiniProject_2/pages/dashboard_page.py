"""
dashboard_pages.py
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from MiniProject_2.common import Config

class DashboardPage:
    """Represents the dashboard page and provides methods to interact with menu items."""
    def __init__(self, driver):
        """Initializes the DashboardPage with the given WebDriver instance."""
        self.driver = driver
        self.menu_items = {
            "Admin": Config.ADMIN_BUTTON,
            "PIM": Config.PIM_BUTTON,
            "Leave": Config.LEAVE_BUTTON,
            "Time": Config.TIME_BUTTON,
            "Recruitment": Config.RECRUITMENT_BUTTON,
            "My Info": Config.MY_INFO_BUTTON,
            "Performance": Config.PERFORMANCE_BUTTON,
            "Dashboard": Config.DASHBOARD_BUTTON,
        }

    def verify_menu_item_clickable(self, menu_name):
        """
        Verifies if a menu item is clickable on the dashboard.
        Args: menu_name (str): The name of the menu item to verify.
        Returns: bool: True if the menu item is clickable, False otherwise.
        """
        menu_locator = self.menu_items.get(menu_name)
        if not menu_locator:
            raise ValueError(f"Menu item '{menu_name}' does not exist in the menu items list.")
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, menu_locator)))