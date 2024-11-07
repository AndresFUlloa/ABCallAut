from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class CreateUserPage(BasePage):

    def __init__(self):
        super().__init__()
        self.ID_NUMBER = (By.CSS_SELECTOR, "input[formcontrolname='id_number']")
        self.NAME = (By.CSS_SELECTOR, "input[formcontrolname='name']")
        self.LAST_NAME = (By.CSS_SELECTOR, "input[formcontrolname='last_name']")
        self.EMAIL = (By.CSS_SELECTOR, "input[formcontrolname='email']")
        self.CELLPHONE = (By.CSS_SELECTOR, "input[formcontrolname='cellphone']")
        self.PASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='password']")
        self.CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='password2']")
        self.ROLE = (By.XPATH, "//mat-label[text()='Seleccione Tipo De perfil']")
        self.ID_TYPE = (By.XPATH, "//mat-label[text()='Seleccione tipo de Identificación']")
        self.SAVE_BUTTON = (By.TAG_NAME, "button")

    def set_id_number(self, id_number: str):
        DriverUtils.wait_until_clickable(self.ID_NUMBER).send_keys(id_number)

    def set_name(self, name: str):
        DriverUtils.wait_until_clickable(self.NAME).send_keys(name)

    def set_last_name(self, last_name: str):
        DriverUtils.wait_until_clickable(self.LAST_NAME).send_keys(last_name)

    def set_email(self, email: str):
        DriverUtils.wait_until_clickable(self.EMAIL).send_keys(email)

    def set_cellphone(self, cellphone: str):
        DriverUtils.wait_until_clickable(self.CELLPHONE).send_keys(cellphone)

    def set_password(self, password: str):
        DriverUtils.wait_until_clickable(self.PASSWORD).send_keys(password)

    def set_confirm_password(self, password: str):
        DriverUtils.wait_until_clickable(self.CONFIRM_PASSWORD).send_keys(password)

    def set_id_type(self, id_type: str):
        DriverUtils.select_by_mat_selector(self.ID_TYPE, id_type)

    def set_role(self, role: str):
        DriverUtils.select_by_mat_selector(self.ROLE, role)

    def click_guardar(self):
        DriverUtils.wait_until_clickable(self.SAVE_BUTTON).click()