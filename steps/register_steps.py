from behave import when
from faker import Faker

from pages.register_page import RegisterPage

fake = Faker()


@when('user fills the register form with "{id_type}", "{id_number}", "{name}", "{last_name}", "{company}", '
      '"{communication_type}", "{email}", "{cellphone}", "{password}"')
def step_user_fills_register_form(context, id_type, id_number, name, last_name, company, communication_type, email,
                                  cellphone, password):
    context.register_page = RegisterPage()
    context.register_page.set_id_type(id_type)

    if id_number == "rand":
        id_number = fake.random_number(digits=10)
    context.register_page.set_id_number(id_number)

    if name == 'rand':
        name = fake.name()
    context.register_page.set_name(name)

    if last_name == 'rand':
        last_name = fake.last_name()
    context.register_page.set_last_name(last_name)

    context.register_page.set_company(company)
    context.register_page.set_communication_type(communication_type)

    if email == 'rand':
        name.replace(" ", "_")
        email = f"{name.lower()}.{last_name.lower()}@{fake.word()}.com"
    context.register_page.set_email(email)

    if cellphone == 'rand':
        cellphone = fake.random_number(10)
    context.register_page.set_cellphone(cellphone)

    context.register_page.set_password(password)
    context.register_page.set_confirm_password(password)

    context.register_page.click_submit()

