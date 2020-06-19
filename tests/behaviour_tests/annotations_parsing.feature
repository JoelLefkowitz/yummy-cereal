Feature: Annotations parsing
    Parsing objects from class annotations

Scenario: Parsing a menu from a yaml file
    Given I have annotated menu classes
    And I have a serealized menu
    When I create a menu parser
    And I parse the serealized menu
    Then I recieve a menu object
