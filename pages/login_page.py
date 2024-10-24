from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.driver_utils import DriverUtils


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.LOGIN_USER = (By.ID, "usuario")
        self.LOGIN_PASSWORD = (By.ID, "contrasena")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def set_user(self, username):
        DriverUtils.wait_for_element(self.LOGIN_USER).send_keys(username)

    def set_password(self, password):
        DriverUtils.wait_for_element(self.LOGIN_PASSWORD).send_keys(password)

    def click_login(self):
        DriverUtils.wait_for_element(self.LOGIN_BUTTON).click()
