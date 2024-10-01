from utils.driver_utils import DriverUtils
from behave import given


@given("the user starts the app")
def iniciar_app(context):
    driver = DriverUtils.set_driver()
    driver.maximize_window()
    driver.get('https://automationexercise.com/')