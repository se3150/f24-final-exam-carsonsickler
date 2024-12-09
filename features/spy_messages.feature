Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the 0 option for element "select#decoder-setting"
    And I select the option with the value "3" for element "select#shift-amount"
    And I type "Hello World!" in the message box
    And I click on the button "button#submit"
    And I wait for 100 milliseconds
    Then I expect that element "#decoded_message" contains the text "Khoor Zruog!"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the 1 option for element "select#decoder-setting"
    And I select the option with the value "3" for element "select#shift-amount"
    And I type "Khoor Zruog!" in the message box
    And I click on the button "button#submit"
    And I wait for 100 milliseconds
    Then I expect that element "#decoded_message" contains the text "Hello World!"
