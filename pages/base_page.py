from selenium.webdriver.common.by import By

from utils.driver_utils import DriverUtils


class BasePage:

    def __init__(self):
        self.SPINNER = (By.CSS_SELECTOR, "div.spinner-container mat-spinner")
        self.OK_DIALOG_BUTTON = (By.CSS_SELECTOR, "mat-dialog-container button")

    def wait_spinner_fade_out(self):
        spinner = DriverUtils.wait_for_element(self.SPINNER)
        DriverUtils.wait_to_fade_out(spinner)

    def click_on_ok(self):
        DriverUtils.wait_until_clickable(self.OK_DIALOG_BUTTON).click()