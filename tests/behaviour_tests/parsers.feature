Feature: Parser factories
    Parsing and validating data from class annotations

Scenario: Parsing a menu
    Given I have annotated menu classes
    When I create a menu parser
    And I parse a menu
    Then The menu data is validated
    And I recieve menu objects
