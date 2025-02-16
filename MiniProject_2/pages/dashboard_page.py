"""
dashboard_pages.py
Page Object for dashboard interactions.
"""

from selenium.webdriver.common.by import By
from MiniProject_2.common import Config
from MiniProject_2.pages.base_page import BasePage

class DashboardPage(BasePage):
    """Represents the dashboard page and provides methods to interact with menu items."""
    def __init__(self, driver):
        """Initializes the DashboardPage with the given WebDriver instance."""
        super().__init__(driver, timeout=Config.DEFAULT_TIMEOUT)
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
        self.wait_for_element((By.XPATH, menu_locator), condition='clickable')