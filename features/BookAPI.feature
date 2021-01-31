Feature: Verify if Books are added and deleted using Library API

    @library
    Scenario: Verify AddBook functionality
        Given The Book details which needs to be added
        When We execute the AddBook API method
        Then the book is successfully added
        And status code of response should be 200

    @library
    Scenario Outline: Verify AddBooks functionality
        Given The Book details with <isbn> and <aisle> needs to be added
        When We execute the AddBook API method
        Then the book is successfully added
            Examples:
                | isbn       | aisle    |
                | testdata5  | 1063897  |
                | testdata6  | 1063898  |