import datetime
import time

from behave import then, when
from selenium.webdriver.remote.webelement import WebElement

from pages.check_pqr_page import CheckPQRPage
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
    time.sleep(5)




