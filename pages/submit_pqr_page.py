from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class SubmitPQRPage(BasePage):

    def __init__(self):
        super().__init__()
        # (By.ID, "mat-mdc-form-field-label-2")
        self.REQUEST_TYPE = (By.CSS_SELECTOR, "select[formcontrolname='type']")
        # (By.ID, "mat-input-0")
        self.SUBJECT = (By.CSS_SELECTOR, "input[formcontrolname='title']")
        # (By.ID, "mat-input-1")
        self.DESCRIPTION = (By.ID, "descripcion")
        self.SEND_BUTTON = (By.TAG_NAME, "button")
        self.TRACKING_NUMBER = (By.CSS_SELECTOR, "mat-dialog-container p")

    def set_request_type(self, request_type):
        DriverUtils.select_by_value(self.REQUEST_TYPE, request_type)

    def set_subject(self, subject):
        DriverUtils.wait_for_element(self.SUBJECT).send_keys(subject)

    def set_description(self, description):
        DriverUtils.wait_for_element(self.DESCRIPTION).send_keys(description)

    def click_on_send(self):
        DriverUtils.wait_until_clickable(self.SEND_BUTTON).click()

    def get_tracking_number(self) -> WebElement:
        return DriverUtils.wait_until_visible(self.TRACKING_NUMBER)

