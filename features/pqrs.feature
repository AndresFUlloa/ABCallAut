Feature: Submit PQRS

    @Test
    Scenario: Submit PQR correctly
        Given the user starts the app
        When user set email "robert@mail.com"
        And user set password "Test@123"
        And user clicks login button
        And user navigates to "Radicar PQR"
        And user selects pqr request type "rand"
        And user set pqr subject "rand"
        And user set pqr description "rand"
        And user clicks on send pqr
        Then tracking number must be visible
        When user navigates to "Consultar PQR"
        And user search ticket number "Global"
        Then Pqr subject must be "Global"
        And Pqr Status must be "ABIERTO"
        And Pqr Date must be "TODAY"
        When user clicks on details
        Then validate details fields "Global", "Global", "Global", "OPEN", "TODAY", "Global"