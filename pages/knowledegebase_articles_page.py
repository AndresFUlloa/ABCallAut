from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.list_page import ListPage
from utils.driver_utils import DriverUtils


class KnowledgebaseArticlesPage(ListPage):

    def __init__(self):
        super().__init__()
        self.SEARCH_INPUT = (By.ID, "search-content")
        self.SEARCH_BUTTON = (By.CSS_SELECTOR, "button.ml-3")

    def input_search(self, search_text: str):
        DriverUtils.wait_until_visible(self.SEARCH_INPUT).send_keys(search_text)

    def click_on_search(self):
        DriverUtils.wait_until_clickable(self.SEARCH_BUTTON).click()

    def click_on_see_more(self, row: int):
        locator = (By.CSS_SELECTOR, self._get_row_locator(row) + ' td:nth-child(2) > [href="javascript:void(0)"]')
        DriverUtils.wait_until_clickable(locator).click()

    def get_content(self, row: int) -> WebElement:
        locator = (By.CSS_SELECTOR, self._get_row_locator(row) + ' td:nth-child(2)')
        return DriverUtils.wait_until_visible(locator)
