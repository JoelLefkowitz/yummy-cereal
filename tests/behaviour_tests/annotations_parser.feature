Feature: Annotations parser factory
    Parsing data from class annotations

Scenario: Parsing a menu
    Given I have annotated menu classes
    When I create a menu parser
    And I parse a menu
    Then I recieve menu objects
