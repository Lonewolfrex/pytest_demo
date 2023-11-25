from selenium import webdriver

class Utilities:
    @staticmethod
    def initialize_driver(browser_type="firefox"):
        if browser_type.lower() == "chrome":
            driver_path = "/home/parrot/Desktop/Demos/pytest_demo/chromedriver"
            return webdriver.Chrome(executable_path=driver_path)
        elif browser_type.lower() == "firefox":
            driver_path = "/home/parrot/Desktop/Demos/pytest_demo/geckodriver"
            driver = webdriver.Firefox(executable_path=driver_path)
        else:
            raise ValueError("Invalid browser type. Supported types: 'chrome' or 'firefox'")
            driver = NULL
        return driver
           
    @staticmethod
    def quit_driver(driver):
        driver.quit()

    @staticmethod
    def close_driver(driver):
        driver.close()

    @staticmethod
    def window_maximize(driver):
        driver.maximize_window()
