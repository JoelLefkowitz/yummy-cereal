Feature: Validated parser factory
    Attatch validation checks to a parser

Scenario: Validating a menu
    Given I have a menu parser
    And I create a validated parser
    When I parse and validate a menu
    Then Validation checks are run
