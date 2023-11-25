from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demo.openmrs.org/openmrs/referenceapplication/home.page"
        self.logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
    
    def assert_successful_navigation(self, browser):
        assert "Home" in browser.title