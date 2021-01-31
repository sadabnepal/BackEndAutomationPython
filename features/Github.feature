Feature: Github validation

    Scenario: Session Management Check
        Given I pass username and password github auth credentials
            | username  	  | password        |
            | <YOUR_USERNAME> | <YOUR_PASSWORD> |
        When I hit getRepo API of github
        Then status code of response should be 200