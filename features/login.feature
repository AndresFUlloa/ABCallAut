Feature: Login in to ABCall

    @Regression
    Scenario: Login correctly
        Given the user starts the app
        When user set email "andresulloa@test.com"
        And user set password "ABCpassword123!"
        And user clicks login button
