import time

from behave import when

from pages.navigation_page import NavigationPage


@when('user navigates to "{link_name}"')
def navigate_to(context, link_name):
    context.navigation_page = NavigationPage()
    context.navigation_page.navigate_to(link_name.upper())
    time.sleep(5)
