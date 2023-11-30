from selenium import webdriver
from PIL import Image
import os
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

class Utilities:

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
           
    
    def quit_driver(driver):
        driver.quit()
        print("Driver has quit. Session closed! ")

    
    def close_driver(driver):
        driver.close()
        print("Driver has closed. Browser closed! ")

    
    def window_maximize(driver):
        driver.maximize_window()

    def create_screenshot_directory(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created.")
        else:
            print(f"Directory '{directory_path}' already exists.")        

    def combine_images(TC_name):
        src_dir = "screenshots/"
        dest_directory = "screenshots/"+TC_name
        file_name = TC_name+".png"
        # Create the destination directory with a timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        dest_dir_with_timestamp = os.path.join(dest_directory, f'Executed_On_{timestamp}')
        os.makedirs(dest_dir_with_timestamp, exist_ok=True)

        # Get a list of all files in the source directory
        files = os.listdir(src_dir)

        # Filter out non-image files (you can extend this list if needed)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not image_files:
            print("No image files found in the source directory.")
            return

        images = []

        for image_file in image_files:
            image_path = os.path.join(src_dir, image_file)

            # Open each image and append it to the list
            img = Image.open(image_path)
            images.append(img)

        # Determine the size of the final image based on the first image
        width, height = images[0].size

        # Create a new image with the determined size
        combined_image = Image.new('RGB', (width * len(images), height))

        # Paste each image into the combined image
        for i, img in enumerate(images):
            combined_image.paste(img, (i * width, 0))

        # Save the combined image to the specified destination directory and file name
        combined_image_path = os.path.join(dest_dir_with_timestamp, file_name)
        combined_image.save(combined_image_path)

        for image_file in image_files:
            image_path = os.path.join(src_dir, image_file)
            os.remove(image_path)

    
    def custom_launch_url(self, driver, url):
        driver.get(url)
        print(f"{url} launched successfully.") 

    
    def custom_wait(self, driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    
    def custom_is_element_visible(self, driver, locator, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutError:
            print(f"{locator} is not visible.")            
            return False

    
    def custom_is_element_interactable(self, driver, locator, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutError:
            print(f"{locator} is not interactable.")            
            return False

    
    def custom_element_ready_to_be_used(self, driver, locator):
        element_visible = self.custom_is_element_visible(driver, locator)
        element_interactable = self.custom_is_element_interactable(driver,locator)
        if ((element_visible == True) and (element_interactable==True)):
            return True
        else:
            print(f"{locator} cannot be used!")
            return False

    
    def custom_click(self, driver, locator):
        if(self.custom_element_ready_to_be_used(driver, locator) == True):
            element = self.custom_wait(driver, locator)
            element.click()
            print(f"{locator} clicked successfully.")
        else:
            print(f"{locator} click failed.")

    
    def custom_fill_field(self, driver, locator, text):
        if(self.custom_element_ready_to_be_used(driver, locator) == True):
            element = self.custom_wait(driver, locator)
            element.clear()
            element.send_keys(text)
            print(f"Text {text} inserted in {locator} successfully.")
        else:
            print(f"Text failed to insert in {locator}.") 