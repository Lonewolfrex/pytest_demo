from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.common_utilities import Utilities

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utilities()
        self.url = "https://demo.openmrs.org/openmrs/login.htm"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
        self.location_button = (By.ID, "Laboratory")
        self.login_error_msg_text = (By.ID, "error-message")
        self.location_not_selected_error_msg_text = (By.ID, "sessionLocationError")

    def open_login_page(self):
        self.utils.custom_launch_url(self.driver,self.url)

    def login(self, username, password):
        self.utils.custom_fill_field(self.driver,self.username_input, username)
        self.utils.custom_fill_field(self.driver,self.password_input, password)
        self.utils.custom_click(self.driver,self.location_button)
        self.utils.custom_click(self.driver,self.login_button)

    def no_location_login(self, username, password):
        self.utils.custom_fill_field(self.driver,self.username_input, username)
        self.utils.custom_fill_field(self.driver,self.password_input, password)
        self.utils.custom_click(self.driver,self.login_button)

    def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button)
        )

    def assert_invalid_credential_msg(self):
        assert "Invalid username/password. Please try again." in self.driver.find_element(*self.login_error_msg_text).text

    def assert_select_location_msg(self):
        assert "You must choose a location!" in self.driver.find_element(*self.location_not_selected_error_msg_text).text

    def assert_successful_navigation(self, browser):
        assert "Login" in browser.title