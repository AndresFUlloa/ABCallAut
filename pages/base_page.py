from selenium.webdriver.common.by import By

from utils.driver_utils import DriverUtils


class BasePage:

    def __init__(self):
        self.SPINNER = (By.CSS_SELECTOR, "div.spinner-container mat-spinner")

    def wait_spinner_fade_out(self):
        spinner = DriverUtils.wait_for_element(self.SPINNER)
        DriverUtils.wait_to_fade_out(spinner)