from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.LOGIN_USER = (By.ID, "usuario")
        self.LOGIN_PASSWORD = (By.ID, "contrasena")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.REGISTER_LINK = (By.CLASS_NAME, "registro-link")

    def set_user(self, username):
        DriverUtils.wait_for_element(self.LOGIN_USER).send_keys(username)

    def set_password(self, password):
        DriverUtils.wait_for_element(self.LOGIN_PASSWORD).send_keys(password)

    def click_login(self):
        DriverUtils.wait_for_element(self.LOGIN_BUTTON).click()

    def click_register(self):
        DriverUtils.wait_for_element(self.REGISTER_LINK).click()
