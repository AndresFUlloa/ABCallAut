Feature: Register in to ABCall

    @Regression
    Scenario Outline: Register correctly
        Given the user starts the app
        When user clicks on register
        And user fills the register form with "<id_type>", "<id_number>", "<name>", "<last_name>", "<company>", "<communication_type>", "<email>", "<cellphone>", "<password>"
        And user set email "global"
        And user set password "global"
        And user clicks login button

    Examples:
        |id_type| id_number    | name       | last_name | company          | communication_type | email                | cellphone     | password        |
        | Cedula | rand        | rand       | rand      | TIGO | Sms | rand | rand | ABCpassword123! |