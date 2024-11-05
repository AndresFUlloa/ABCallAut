from behave import given, when

from pages.login_page import LoginPage
from utils import global_variable
from utils.config_properties import ConfigProperties
from utils.driver_utils import DriverUtils

login_page: LoginPage


@given("the user starts the app")
def start_app(context):
    config_properties = ConfigProperties()
    DriverUtils.set_driver()
    DriverUtils.driver.maximize_window()
    DriverUtils.driver.get(config_properties.get_home_url())


@when('user set email "{email}"')
def set_email(context, email):
    context.loginPage = LoginPage()
    if email.lower() == 'global':
        email = global_variable.NEW_USER.email
    context.loginPage.set_user(email)


@when('user set password "{password}"')
def set_password(context, password):
    context.loginPage = LoginPage()
    if password.lower() == 'global':
        password = global_variable.NEW_USER.password
    context.loginPage.set_password(password)


@when('user clicks login button')
def click_login(context):
    context.loginPage = LoginPage()
    context.loginPage.click_login()
    context.loginPage.wait_spinner_fade_out()


@when('user clicks on register')
def click_register(context):
    context.loginPage = LoginPage()
    context.loginPage.click_register()
