from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.utilities import Utilities
import pytest
import datetime
import inspect
from selenium import webdriver

@pytest.fixture
def browser():
    driver = Utilities.initialize_driver("chrome")
    Utilities.window_maximize(driver)
    yield driver

    Utilities.quit_driver(driver)

@pytest.mark.parametrize("username, password", [("admin", "Admin123")])
def test_TC1_successful_login_logout(browser, username, password):
    TC_name = inspect.currentframe().f_code.co_name
    src_path = "screenshots"

    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step1.png")
    login_page.login("admin", "Admin123")
    browser.save_screenshot(src_path+"/Step2.png")
    home_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step3.png")
    home_page.logout()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step4.png")

    Utilities.combine_images(TC_name)

@pytest.mark.parametrize("username, password", [("admin123", "Admin123"), ("admin", "Admin1234"),("admin123", "Admin1234"),("", "")])
def test_TC2_incorrect_credential_login(browser, username, password):
    TC_name = inspect.currentframe().f_code.co_name
    src_path = "screenshots"

    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step1.png")    
    login_page.login(username, password)
    login_page.assert_invalid_credential_msg()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step2.png")  

    Utilities.combine_images(TC_name)  

def test_TC3_test_no_location_login(browser):
    TC_name = inspect.currentframe().f_code.co_name
    src_path = "screenshots"

    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.wait_for_login_page()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step1.png")      
    login_page.no_location_login("admin", "Admin123")
    login_page.assert_select_location_msg()
    login_page.assert_successful_navigation(browser)
    browser.save_screenshot(src_path+"/Step2.png")  

    Utilities.combine_images(TC_name)
