import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self, direction='down', scroll_amount=1000):
        """
        Scrolls the page up or down.

        :param direction: 'up' to scroll up, 'down' to scroll down.
        :param scroll_amount: Number of pixels to scroll in each step.
        """
        if direction not in ['up', 'down']:
            raise ValueError("Direction must be either 'up' or 'down'.")

        # Get the current scroll position
        current_scroll_position = self.driver.execute_script("return window.pageYOffset;")
        match = False

        while not match:
            last_scroll_position = current_scroll_position
            time.sleep(1)  # Wait to allow for scrolling

            if direction == 'down':
                # Scroll down by the specified pixel value
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            else:  # direction == 'up'
                # Scroll up by the specified pixel value
                self.driver.execute_script(f"window.scrollBy(0, -{scroll_amount});")

            time.sleep(1)  # Allow time for the page to adjust after scrolling
            current_scroll_position = self.driver.execute_script("return window.pageYOffset;")

            # Get the total height of the page
            page_height = self.driver.execute_script("return document.body.scrollHeight;")

            # Check exit conditions based on the scroll direction
            if direction == 'down':
                if current_scroll_position + scroll_amount >= page_height or last_scroll_position == current_scroll_position:
                    match = True
            else:  # direction == 'up'
                if current_scroll_position == 0 or last_scroll_position == current_scroll_position:
                    match = True

        time.sleep(4)  # Allow time for any final rendering

    def wait_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_visibility_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

    def wait_presence_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return element

    def wait_url_contains(self, url):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.url_contains(url))
        return element