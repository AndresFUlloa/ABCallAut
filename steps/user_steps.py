import time
import random

from behave import when, then
from faker import Faker
from selenium.common import TimeoutException

from dtos.user_dto import UserDTO
from pages.create_user_page import CreateUserPage
from pages.user_list_page import UserListPage
from utils import global_variable

fake = Faker()


@when('user click on create user')
def user_clicks_create_user(context):
    context.user_list_page = UserListPage()
    context.user_list_page.click_create_user()


@when('user creates user with "{id_number}", "{name}", "{last_name}", "{email}", "{cellphone}", "{password}", '
      '"{id_type}", and "{role}"')
def user_creates_user(context, id_number, name, last_name, email, cellphone, password, id_type, role):
    context.create_user_page = CreateUserPage()
    id_types = ['Cedula', 'Passport', 'Cedula_extranjeria']
    global_variable.NEW_USER = UserDTO()

    if id_number == 'rand':
        id_number = fake.random_number(digits=10)
    global_variable.NEW_USER.id_number = id_number

    if name == 'rand':
        name = fake.name()
    global_variable.NEW_USER.name = name

    if last_name == 'rand':
        last_name = fake.last_name()
    global_variable.NEW_USER.last_name = last_name

    if email == 'rand':
        temp_name = name.replace(" ", "_")
        email = f"{temp_name.lower()}.{last_name.lower()}@{fake.word().lower()}.com"
    global_variable.NEW_USER.email = email

    if cellphone == 'rand':
        cellphone = f"{fake.random_number(10)}"
    global_variable.NEW_USER.cellphone = cellphone

    if id_type == 'rand':
        id_type = id_types[random.choice([0, 1, 2])]
        print("ID TYPE:", id_type)
    global_variable.NEW_USER.id_type = id_type

    global_variable.NEW_USER.role = role

    context.create_user_page.set_id_number(id_number)
    context.create_user_page.set_name(name)
    context.create_user_page.set_last_name(last_name)
    context.create_user_page.set_email(email)
    context.create_user_page.set_cellphone(cellphone)
    context.create_user_page.set_password(password)
    context.create_user_page.set_confirm_password(password)
    context.create_user_page.set_id_type(id_type)
    context.create_user_page.set_role(role)
    context.create_user_page.click_guardar()
    context.create_user_page.wait_spinner_fade_out()
    context.create_user_page.click_on_ok()


@when('user search for last user')
def user_search_for_last_user(context):
    context.user_list_page = UserListPage()
    context.user_list_page.click_last_page()


@then('user in list must be "{id_number}", "{name}", "{role}"')
def user_in_list_must_be(context, id_number, name, role):
    time.sleep(3)
    context.user_list_page = UserListPage()

    if id_number.lower() == 'global':
        id_number = global_variable.NEW_USER.id_number

    if name.lower() == 'global':
        name = f"{global_variable.NEW_USER.name} {global_variable.NEW_USER.last_name}"

    if role.lower() == 'global':
        role = global_variable.NEW_USER.role

    element = context.user_list_page.get_id_number('last')
    assert element.is_displayed(), "Id number is not visible"
    assert element.text == id_number, f"Id number invalid expected: {id_number}, got {element.text} instead"

    element = context.user_list_page.get_name('last')
    assert element.is_displayed(), "Name is not visible"
    assert element.text == name, f"Name invalid expected: {name}, got {element.text} instead"

    element = context.user_list_page.get_perfil('last')
    assert element.is_displayed(), "Role is not visible"
    assert element.text == role, f"Role invalid expected: {role}, got {element.text} instead"
