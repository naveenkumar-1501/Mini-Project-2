import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject_2.pages.dashboard_page import DashboardPage
from MiniProject_2.pages.login_page import LoginPage
from MiniProject_2.common import Config

@pytest.mark.usefixtures("driver")
class TestMenus:
    def test_menu_items_clickable(self, driver):
        """Test to verify all menu items are clickable."""
        # Navigate to the URL
        driver.get(Config.URL)
        # Log in first to ensure we're on the dashboard
        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")
        # Ensure we are redirected to the dashboard after login
        WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, Config.DASHBOARD_BUTTON)))
        # Debugging: Print page source after login to check if the dashboard is correctly loaded
        print("Page source after login:")
        print(driver.page_source)
        # Initialize DashboardPage after login
        dashboard_page = DashboardPage(driver)
        # Menu items and their respective XPaths
        menu_items_xpaths = {
            "Admin": Config.ADMIN_BUTTON,
            "PIM": Config.PIM_BUTTON,
            "Leave": Config.LEAVE_BUTTON,
            "Time": Config.TIME_BUTTON,
            "Recruitment": Config.RECRUITMENT_BUTTON,
            "My Info": Config.MY_INFO_BUTTON,
            "Performance": Config.PERFORMANCE_BUTTON,
            "Dashboard": Config.DASHBOARD_BUTTON
        }
        # Print menu items for debugging
        print("Menu items and their XPaths:")
        for menu, xpath in menu_items_xpaths.items():
            print(f"{menu}: {xpath}")
        # Loop through menu items and verify they are clickable
        for menu, xpath in menu_items_xpaths.items():
            self.verify_and_click_menu(driver, menu, xpath, dashboard_page)

    def verify_and_click_menu(self, driver, menu, xpath, dashboard_page):
        """Helper function to verify and click a menu item."""
        try:
            print(f"Checking if {menu} is clickable with XPath: {xpath}...")
            menu_element = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            print(f"Successfully found and clicked on {menu}.")
            menu_element.click()
            dashboard_page.verify_menu_item_clickable(menu)
        except Exception as error:
            print(f"Error with {menu} menu: {error}")
            pytest.fail(f"Menu item '{menu}' was not clickable. XPath: {xpath}. Error: {error}")
