import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


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
    def wait_for_element(locator: tuple[str, str], timeout=10) -> WebElement:
        return WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_until_visible(locator: tuple[str, str], timeout=10) -> WebElement:
        return WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_until_clickable(locator: tuple, timeout=10) -> WebElement:
        return WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))

    @staticmethod
    def wait_to_fade_out(element: WebElement, timeout=180):
        WebDriverWait(DriverUtils.driver, timeout).until(
            expected_conditions.invisibility_of_element(element)
        )

    @staticmethod
    def select_by_value(locator: tuple[str, str], value: str):
        element = DriverUtils.wait_for_element(locator)
        select = Select(element)
        select.select_by_value(value)

    @staticmethod
    def select_by_index(locator: tuple[str, str], index: int):
        element = DriverUtils.wait_for_element(locator)
        select = Select(element)
        select.select_by_index(index)

    @staticmethod
    def select_by_visible_text(locator: tuple[str, str], text: str):
        element = DriverUtils.wait_for_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    @staticmethod
    def select_by_mat_selector(locator: tuple, text: str):
        DriverUtils.wait_until_clickable(locator).click()
        xpath = (By.XPATH, f'//*[text()="{text}"]')
        DriverUtils.wait_until_clickable(xpath).click()

    @staticmethod
    def take_screenshot(name: str):
        pass
