import random
import time

from behave import when, then
from faker import Faker
from selenium.webdriver.remote.webelement import WebElement

from dtos.pqr_dto import PqrDTO
from pages.submit_pqr_page import SubmitPQRPage
from utils import global_variable

fake = Faker()
PQRS_Types = ["Peticion", "Queja", "Reclamo"]


@when('user selects pqr request type "{request_type}"')
def step_set_request_type(context, request_type):
    global_variable.NEW_PQR = PqrDTO()
    if request_type == 'rand':
        request_type = PQRS_Types[random.choice([0, 1, 2])]
    context.submit_page = SubmitPQRPage()
    print("REQUEST TYPE:", request_type)
    context.submit_page.set_request_type(request_type)
    global_variable.NEW_PQR.type = request_type


@when('user set pqr subject "{subject}"')
def step_set_subject(context, subject):
    if subject == 'rand':
        subject = fake.word()
    context.submit_page.set_subject(subject)
    global_variable.NEW_PQR.subject = subject


@when('user set pqr description "{description}"')
def step_set_description(context, description):
    if description == 'rand':
        description = fake.text()
    context.submit_page.set_description(description)
    global_variable.NEW_PQR.description = description


@when('user clicks on send pqr')
def click_on_send(context):
    context.submit_page.click_on_send()
    time.sleep(10)


@then('tracking number must be visible')
def check_tracking_number(context):
    tracking_number: WebElement = context.submit_page.get_tracking_number()
    assert tracking_number.is_displayed(), "ID Number Not Found"
    assert "#" in tracking_number.text, "Invalid tracking number"
    global_variable.NEW_PQR.tracking_number = tracking_number.text.split("#")[1]
    context.submit_page.click_on_ok()
