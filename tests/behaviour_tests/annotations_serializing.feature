Feature: Annotations serializing
    Serializing objects from class annotations

Scenario: Serializing a menu to a yaml file
    Given I have annotated menu classes
    And I have a menu object
    When I create a menu serializer
    And I serialize the menu object
    Then I output the serialized menu
