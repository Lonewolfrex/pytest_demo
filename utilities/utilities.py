from selenium import webdriver
from PIL import Image
import os
import datetime

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
        print(f"Combined image saved to: {combined_image_path}")

        for image_file in image_files:
            image_path = os.path.join(src_dir, image_file)
            os.remove(image_path)
            print(f"Deleted image: {image_file}")
            
