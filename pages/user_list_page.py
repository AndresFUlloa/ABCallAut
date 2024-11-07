from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class UserListPage(BasePage):

    def __init__(self):
        super().__init__()
        self.CREATE_USER_BUTTON = (By.CLASS_NAME, "button-1")
        self.LAST_PAGE_BUTTON = (By.CLASS_NAME, "mat-mdc-paginator-navigation-last")
        self.ROWS_LOCATOR = "tbody > tr"

    def click_create_user(self):
        DriverUtils.wait_until_clickable(self.CREATE_USER_BUTTON).click()

    def click_last_page(self):
        DriverUtils.wait_until_clickable(self.LAST_PAGE_BUTTON).click()

    def _get_row_locator(self, row) -> str:
        row_locator = self.ROWS_LOCATOR
        if row == 'last':
            row_locator += ":last-child"
        else:
            if not isinstance(row, int):
                raise TypeError("Row attribute must be number")
            row_locator += f':nth-child({row})'

        return row_locator

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


