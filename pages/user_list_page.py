from typing import Optional

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.list_page import ListPage
from utils.driver_utils import DriverUtils


class UserListPage(ListPage):

    def __init__(self):
        super().__init__()
        self.CREATE_USER_BUTTON = (By.CLASS_NAME, "button-1")

    def click_create_user(self):
        DriverUtils.wait_until_clickable(self.CREATE_USER_BUTTON).click()

    def get_id_number(self, row) -> WebElement:
        row_locator = self._get_row_locator(row)
        row_locator += " > td:first-child"
        locator = (By.CSS_SELECTOR, row_locator)
        return DriverUtils.wait_until_visible(locator)

    def get_name(self, row) -> WebElement:
        row_locator = self._get_row_locator(row)
        row_locator += " > td:nth-child(2)"
        locator = (By.CSS_SELECTOR, row_locator)
        return DriverUtils.wait_until_visible(locator)

    def get_perfil(self, row) -> WebElement:
        row_locator = self._get_row_locator(row)
        row_locator += " > td:nth-child(3)"
        locator = (By.CSS_SELECTOR, row_locator)
        return DriverUtils.wait_until_visible(locator)

    def click_edit(self, row):
        row_locator = self._get_row_locator(row)
        row_locator += " > td:nth-child(4) button:first-child"
        locator = (By.CSS_SELECTOR, row_locator)
        DriverUtils.wait_until_clickable(locator).click()

    def is_id_number_in_table(self, id_number: str) -> Optional[WebElement]:
        locator = (By.XPATH, f"//tbody/tr/td[1][text()=' {id_number} ']")
        try:
            return DriverUtils.wait_until_visible(locator, timeout=1)
        except TimeoutException as ex:
            return None

    def get_id_number_from_row(self, row: WebElement):
        return self.get_td_from_row(row, 1)

    def get_name_from_row(self, row: WebElement):
        return self.get_td_from_row(row, 2)

    def get_role_from_row(self, row: WebElement):
        return self.get_td_from_row(row, 3)