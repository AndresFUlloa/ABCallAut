Feature: Register in to ABCall

    @Regression
    Scenario Outline: Register correctly
        Given the user starts the app
        When user clicks on register
        And user fills the register form with "<id_type>", "<id_number>", "<name>", "<last_name>", "<company>", "<communication_type>", "<email>", "<cellphone>", "<password>"

    Examples:
        |id_type| id_number    | name       | last_name | company          | communication_type | email                | cellphone     | password        |
        | Cedula | rand        | rand       | rand      | Movistar | Sms | rand | rand | ABCpassword123! |