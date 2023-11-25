from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demo.openmrs.org/openmrs/login.htm"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
        self.location_button = (By.ID, "Laboratory")
        self.login_error_msg_text = (By.ID, "error-message")
        self.location_not_selected_error_msg_text = (By.ID, "sessionLocationError")

    def open_login_page(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.location_button).click()
        self.driver.find_element(*self.login_button).click()

    def no_location_login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

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
