import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CustomTools.UniversalLogger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    default_timeout = 10

    def do_click(self, by_locator, wait_time=default_timeout):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)).click()

    def do_context_click(self, by_locator, wait_time=default_timeout):
        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).context_click(element).perform()

    def do_send_keys(self, by_locator, text, wait_time=default_timeout):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element(self, by_locator, wait_time=default_timeout):
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))

    def get_elements(self, by_locator, wait_time=default_timeout):
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_all_elements_located(by_locator))

    def get_hidden_element(self, by_locator, wait_time=default_timeout):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(by_locator))

    def get_hidden_elements(self, by_locator, wait_time=default_timeout):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located(by_locator))

    def is_visible(self, by_locator, wait_time=default_timeout):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
            return True
        except Exception as e:
            logger.info(f"Element {by_locator} is not visible. Exception: {e}")
            return False

    def is_clickable(self, by_locator, wait_time=default_timeout):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator))
            return True
        except Exception as e:
            logger.info(f"Element {by_locator} is not clickable. Exception: {e}")
            return False

    def get_current_page_url(self):
        return self.driver.current_url

    def get_current_page_title(self):
        return self.driver.title


