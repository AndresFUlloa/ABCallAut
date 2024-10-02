from utils.config_properties import ConfigProperties
from utils.driver_utils import DriverUtils
from behave import given


@given("the user starts the app")
def start_app(context):
    config_properties = ConfigProperties()
    driver = DriverUtils.set_driver()
    driver.maximize_window()
    driver.get(config_properties.get_home_url())
