from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class CheckPQRPage(BasePage):

    def __init__(self):
        super().__init__()
        self.SEARCH_INPUT = (By.TAG_NAME, "input")
        self.SEND_BUTTON = (By.CSS_SELECTOR, "button.ml-3")

    def search_pqr(self, ticket_number: str):
        DriverUtils.wait_for_element(self.SEARCH_INPUT).send_keys(ticket_number)
        DriverUtils.wait_until_clickable(self.SEND_BUTTON).click()
        self.wait_spinner_fade_out()

    def get_subject_row(self, row: int) -> WebElement:
        locator = (By.CSS_SELECTOR, f"tbody > tr:nth-child({row}) > td:nth-child(1)")
        return DriverUtils.wait_until_visible(locator)

    def get_status_row(self, row: int) -> WebElement:
        locator = (By.CSS_SELECTOR, f"tbody > tr:nth-child({row}) > td:nth-child(2)")
        return DriverUtils.wait_until_visible(locator)

    def get_date_row(self, row: int) -> WebElement:
        locator = (By.CSS_SELECTOR, f"tbody > tr:nth-child({row}) > td:nth-child(3)")
        return DriverUtils.wait_until_visible(locator)

    def click_detail_row(self, row: int):
        locator = (By.CSS_SELECTOR, f"tbody > tr:nth-child({row}) span.mdc-button__label")
        DriverUtils.wait_until_clickable(locator).click()
