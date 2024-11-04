from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.driver_utils import DriverUtils


class RegisterPage(BasePage):

    def __init__(self):
        super().__init__()
        self.ID_TYPE = (By.ID, "tipo-identificacion")
        self.ID_NUMBER = (By.ID, "identificacion")
        self.NAME = (By.ID, "nombres")
        self.LAST_NAME = (By.ID, "apellidos")
        self.COMPANY = (By.ID, "empresa")
        self.COMMUNICATION_TYPE = (By.ID, "tipo-comunicacion")
        self.EMAIL = (By.ID, "correo")
        self.CELLPHONE = (By.ID, "telefono")
        self.PASSWORD = (By.ID, "contrasena")
        self.CONFIRM_PASSWORD = (By.ID, "repetir-contrasena")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def set_id_type(self, id_type):
        DriverUtils.select_by_value(self.ID_TYPE, id_type)

    def set_id_number(self, id_number):
        DriverUtils.wait_for_element(self.ID_NUMBER).send_keys(id_number)

    def set_name(self, name):
        DriverUtils.wait_for_element(self.NAME).send_keys(name)

    def set_last_name(self, last_name):
        DriverUtils.wait_for_element(self.LAST_NAME).send_keys(last_name)

    def set_company(self, company):
        DriverUtils.wait_for_element(self.COMPANY).click()
        DriverUtils.wait_for_element((By.XPATH, f"//option[text()='{company}']")).click()

    def set_communication_type(self, communication_type):
        DriverUtils.select_by_value(self.COMMUNICATION_TYPE, communication_type)

    def set_email(self, email):
        DriverUtils.wait_for_element(self.EMAIL).send_keys(email)

    def set_cellphone(self, cellphone):
        DriverUtils.wait_for_element(self.CELLPHONE).send_keys(cellphone)

    def set_password(self, password):
        DriverUtils.wait_for_element(self.PASSWORD).send_keys(password)

    def set_confirm_password(self, confirm_password):
        DriverUtils.wait_for_element(self.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_submit(self):
        DriverUtils.wait_for_element(self.SUBMIT_BUTTON).click()
