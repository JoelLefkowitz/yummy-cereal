Feature: Validation checks
    Validating an object before parsing it

Scenario: Validating a menu from a yaml file
    Given I have validation checks
    And I have a serealized menu
    And I have a menu parser
    When I create a validator
    And I parse the serealized menu
    Then Validation checks are run
