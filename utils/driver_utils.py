from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCo


class DriverUtils:

    @staticmethod
    def set_driver():
        return webdriver.Chrome()

    @staticmethod
    def close_driver(driver: webdriver):
        driver.quit()

    @staticmethod
    def wait_for_element(driver: webdriver, locator: tuple[str, str], timeout=10):
        return WebDriverWait(driver, timeout).until(
            ExCo.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_until_visible(driver: webdriver, locator: tuple[str, str], timeout):
        return WebDriverWait(driver, timeout).until(
            ExCo.visibility_of_element_located(locator)
        )

    @staticmethod
    def take_screenshot(driver: webdriver, name: str):
        pass
