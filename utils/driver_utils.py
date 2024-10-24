from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DriverUtils:

    driver: webdriver = None

    @staticmethod
    def set_driver(reset=False):
        if reset or DriverUtils.driver is None:
            DriverUtils.driver = webdriver.Chrome()

    @staticmethod
    def close_driver():
        DriverUtils.driver.quit()
        DriverUtils.driver = None

    @staticmethod
    def wait_for_element(locator: tuple[str, str], timeout=10):
        return WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_until_visible(locator: tuple[str, str], timeout):
        return WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @staticmethod
    def take_screenshot(name: str):
        pass
