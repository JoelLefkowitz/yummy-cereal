Feature: Parser
    Create config parsers from simple classes

Scenario: Parsing a menu
    Given I have annotated menu classes
    When I create menu parsers
    And I parse the menu
    Then I recieve menu objects