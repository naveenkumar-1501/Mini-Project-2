"""
common.py
common configuration for web application
"""
class Config:
    """Class to hold constants and configuration details."""
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USER_NAME_FIELD = "//input[@name= 'username']"
    PASSWORD_FIELD = "//input[@name= 'password']"
    LOGIN_BUTTON = "//button[@type ='submit']"
    ADMIN_BUTTON = "//span[text() = 'Admin']"
    PIM_BUTTON = "//span[text() = 'PIM']"
    LEAVE_BUTTON = "//span[text() = 'Leave']"
    TIME_BUTTON = "//span[text() = 'Time']"
    RECRUITMENT_BUTTON = "//span[text() = 'Recruitment']"
    MY_INFO_BUTTON = "//span[text() = 'My Info']"
    PERFORMANCE_BUTTON = "//span[text() = 'Performance']"
    DASHBOARD_BUTTON = "//span[text() = 'Dashboard']"
    ADD_BUTTON = "//button[@class= 'oxd-button oxd-button--medium oxd-button--secondary']"
    FIRST_NAME = "//input[@name = 'firstName']"
    MIDDLE_NAME = "//input[@name= 'middleName']"
    LAST_NAME = "//input[@name= 'lastName']"
    EMPLOYEE_ID = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    TOGGLE_BUTTON = "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']"
    NEW_USERNAME_FIELD = "(//input[@class = 'oxd-input oxd-input--active'])[3]"
    NEW_PASSWORD_FIELD = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    CONFIRM_PASSWORD_FIELD = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    SAVE_BUTTON = "//button[@type= 'submit']"
    SUCCESS_MESSAGE = '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]'
    EMPLOYEE_NAME = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    SEARCH_BUTTON = "//button[@type= 'submit']"
    RECORD = "//div[contains(text(),'Naveen Kumar')]"
    DROP_DOWN_BUTTON = "//span[@class='oxd-userdropdown-tab']"
    LOGOUT_BUTTON = "//a[text()= 'Logout']"
    DEFAULT_TIMEOUT = 20
    PAGE_INDICATOR = "//img[@alt='company-branding']"

