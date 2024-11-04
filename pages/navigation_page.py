from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class NavigationPage(BasePage):

    def __init__(self):
        super().__init__()
        self.nav_dict = {
            "RADICAR PQR": (By.CSS_SELECTOR, "a[href='/createIncidence']"),
            "CONSULTAR PQR": (By.CSS_SELECTOR, "a[href='/listIncidences']"),
            "USUARIOS REGISTRADOS": (By.CSS_SELECTOR, "a[href='/listUsers']"),
            "BASE DE CONOCIMIENTOS": (By.CSS_SELECTOR, "a[href='/articlesList']")
        }

    def navigate_to(self, link_name):
        DriverUtils.wait_until_clickable(self.nav_dict[link_name]).click()
