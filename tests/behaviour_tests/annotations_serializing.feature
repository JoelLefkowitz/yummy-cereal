Feature: Annotations serializing
    Serializing objects from class annotations

Scenario: Serializing a menu
    Given I have annotated menu classes
    And I have a menu object
    When I create a menu serializer
    And I serialize the menu object
    Then I recieve a serialized menu
