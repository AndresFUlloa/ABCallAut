Feature: Search for articles

    @Test
    Scenario Outline: Search Article correctly
        Given the user starts the app
        When user set email "<user>"
        And user set password "<password>"
        And user clicks login button
        And user navigates to "Base de Conocimientos"
        And user search article "<search_text>"
        Then there must be articles

    Examples:
      |user|password|search_text|
      |andresulloa@test.com|ABCpassword123!|PQR|