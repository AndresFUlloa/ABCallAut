import datetime
import time

from behave import then, when
from selenium.webdriver.remote.webelement import WebElement

from pages.check_pqr_page import CheckPQRPage
from pages.pqr_detail_page import DetailPQRPage
from utils import global_variable


@when('user search ticket number "{ticket_number}"')
def search_pqr(context, ticket_number):
    context.check_pqr_page = CheckPQRPage()
    if ticket_number.lower() == 'global':
        ticket_number = global_variable.NEW_PQR.tracking_number

    context.check_pqr_page.search_pqr(ticket_number)


@then('Pqr subject must be "{subject}"')
def check_pqr_subject(context, subject):
    if subject.lower() == 'global':
        subject = global_variable.NEW_PQR.subject

    element: WebElement = context.check_pqr_page.get_subject_row(1)
    assert element.text == subject, f"Subject expected {subject}, got {element.text} instead"


@then('Pqr Status must be "{status}"')
def check_pqrs_status(context, status):
    status = status.upper()
    element: WebElement = context.check_pqr_page.get_status_row(1)
    assert element.text == status, f"Status expected {status}, got {element.text} instead"


@then('Pqr Date must be "{date}"')
def check_pqrs_date(context, date):
    if date.upper() == "TODAY":
        date = datetime.datetime.today().strftime('%Y-%m-%d')
    element: WebElement = context.check_pqr_page.get_date_row(1)
    assert element.text == date, f"Date expected {date}, got {element.text} instead"


@when('user clicks on details')
def click_on_details(context):
    context.check_pqr_page.click_detail_row(1)


@then('validate details fields "{subject}", "{ticket_number}", "{petition_type}", "{state}", "{date}", "{description}"')
def validate_details(context, subject, ticket_number, petition_type, state, date, description):
    context.pqr_detail_page = DetailPQRPage()
    global_str = 'global'
    if subject.lower() == global_str:
        subject = global_variable.NEW_PQR.subject
    if ticket_number.lower() == global_str:
        ticket_number = global_variable.NEW_PQR.tracking_number
    if petition_type.lower() == global_str:
        petition_type = global_variable.NEW_PQR.type
    if date.upper() == "TODAY":
        date = datetime.datetime.today().strftime('%Y-%m-%d')
    if description.lower() == global_str:
        description = global_variable.NEW_PQR.description

    element = context.pqr_detail_page.get_subject()
    assert element.is_displayed(), "Subject is not visible"
    assert element.text == subject, f"Subject expected {subject}, got {element.text} instead"

    element = context.pqr_detail_page.get_ticket()
    assert element.is_displayed(), "Ticket number is not visible"
    assert element.text == ticket_number, f"Ticket number expected {ticket_number}, got {element.text} instead"

    element = context.pqr_detail_page.get_petition()
    assert element.is_displayed(), "Petition type is not visible"
    assert element.text.upper() == petition_type.upper(),\
        f"Petition type expected {petition_type}, got {element.text} instead"

    element = context.pqr_detail_page.get_date()
    assert element.is_displayed(), "Date is not visible"
    assert element.text == date, f"Date expected {date}, got {element.text} instead"

    element = context.pqr_detail_page.get_description()
    assert element.is_displayed(), "Description is not visible"
    assert element.text == description.replace("\n", " "), f'Description expected:\n"{description}",\ngot:\n"{element.text}"\ninstead'
