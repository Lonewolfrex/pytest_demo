from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Provide the path to your GeckoDriver executable here
    driver_path = "/home/parrot/Desktop/Demos/pytest_demo/geckodriver"
    
    # Create a Firefox WebDriver instance
    driver = webdriver.Firefox(executable_path=driver_path)
    
    yield driver
    
    # Close the WebDriver instance after the test
    driver.close()
    driver.quit()

def test_successful_login_logout(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    login_page.login("admin", "Admin123")
    home_page.assert_successful_navigation(browser)
    home_page.logout()
    login_page.assert_successful_navigation(browser)

def test_incorrect_credential_login(browser):
    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    login_page.login("admin", "Admin1234")
    login_page.assert_invalid_credential_msg()
    login_page.assert_successful_navigation(browser)

def test_no_location_login(browser):
    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    login_page.no_location_login("admin", "Admin123")
    login_page.assert_select_location_msg()
    login_page.assert_successful_navigation(browser)

