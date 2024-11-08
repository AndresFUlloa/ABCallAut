from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class ListPage(BasePage):

    def __init__(self):
        super().__init__()
        self.NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Next page']")
        self.LAST_PAGE_BUTTON = (By.CLASS_NAME, "mat-mdc-paginator-navigation-last")
        self.ROWS_LOCATOR = "tbody > tr"
        self.ITEMS_PER_PAGE = (By.CSS_SELECTOR, "mat-select[role='combobox']")

    def click_last_page(self):
        DriverUtils.wait_until_clickable(self.LAST_PAGE_BUTTON).click()

    def get_next_page(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.NEXT_PAGE_BUTTON)

    def _get_row_locator(self, row) -> str:
        row_locator = self.ROWS_LOCATOR
        if row == 'last':
            row_locator += ":last-child"
        else:
            if not isinstance(row, int):
                raise TypeError("Row attribute must be number")
            row_locator += f':nth-child({row})'

        return row_locator

    def select_items_per_page(self, items: str):
        DriverUtils.select_by_mat_selector(self.ITEMS_PER_PAGE, items)

    def get_td_from_row(self, row: WebElement, row_pos: int):
        locator = (By.CSS_SELECTOR, f"td:nth-child({row_pos})")
        return DriverUtils.wait_until_visible(locator=locator, element=row)

    def get_row_from_td(self, td: WebElement):
        locator = (By.XPATH, "..")
        return DriverUtils.wait_until_visible(locator=locator, element=td)