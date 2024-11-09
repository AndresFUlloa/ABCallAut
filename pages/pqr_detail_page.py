from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class DetailPQRPage(BasePage):

    def __init__(self):
        super().__init__()
        self.SUBJECT_LABEL = (By.CSS_SELECTOR, "label.title")
        self.TICKET_LABEL = (By.XPATH, "//label[text()='Ticket:']/parent::div/following-sibling::div/label")
        self.PETITION_LABEL = (By.XPATH, "//label[text()='Tipo:']/parent::div/following-sibling::div/label")
        self.STATE_LABEL = (By.XPATH, "//label[text()='Estado:']/parent::div/following-sibling::div/label")
        self.DATE_LABEL = (By.XPATH, "//label[text()='Fecha:']/parent::div/following-sibling::div/label")
        self.DESCRIPTION_LABEL = (By.XPATH, "//label[text()='Descripción:']/parent::div/following-sibling::div/p")

    def get_subject(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.SUBJECT_LABEL)

    def get_ticket(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.TICKET_LABEL)

    def get_petition(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.PETITION_LABEL)

    def get_state(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.STATE_LABEL)

    def get_date(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.DATE_LABEL)

    def get_description(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.DESCRIPTION_LABEL)
