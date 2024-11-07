Feature: Create User

    @Test
    Scenario: Create user correctly
        Given the user starts the app
        When user set email "andresulloa@test.com"
        And user set password "ABCpassword123!"
        And user clicks login button
        And user navigates to "Usuarios Registrados"
        And user click on create user
        And user creates user with "rand", "rand", "rand", "rand", "rand", "ABCpassword123!", "rand", and "Admin"
        And user navigates to "Usuarios Registrados"
        And user search for last user
        Then user in list must be "Global", "Global", "Global"