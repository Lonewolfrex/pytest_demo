from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.common_utilities import Utilities
from dotenv import load_dotenv
import os

load_dotenv()
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utilities()
        self.url = "https://demo.openmrs.org/openmrs/referenceapplication/home.page"
        self.logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

    def logout(self):
        self.utils.custom_click(self.driver,self.logout_button)
    
    def assert_successful_navigation(self, browser):
        assert "Home" in browser.title