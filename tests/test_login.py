from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.utilities import Utilities
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = Utilities.initialize_driver("chrome")
    Utilities.window_maximize(driver)
    yield driver

    Utilities.quit_driver(driver)

@pytest.mark.parametrize("username, password", [("admin", "Admin123")])
def test_successful_login_logout(browser, username, password):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    login_page.login("admin", "Admin123")
    home_page.assert_successful_navigation(browser)
    home_page.logout()
    login_page.assert_successful_navigation(browser)

@pytest.mark.parametrize("username, password", [("admin123", "Admin123"), ("admin", "Admin1234"),("admin123", "Admin1234"),("", "")])
def test_incorrect_credential_login(browser, username, password):
    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    login_page.login(username, password)
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

