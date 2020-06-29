Feature: Annotations parsing
    Parsing objects from class annotations

Scenario: Parsing a menu from a yaml file
    Given I have annotated menu classes
    And I have a serialized menu
    When I create a menu parser
    And I parse the serialized menu
    Then I recieve a menu object
