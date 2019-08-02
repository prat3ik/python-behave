Feature: testing google

Scenario: Log in with a legitimate user
	Given I enter "valid_user" in "username"
	And I enter "valid_password" in "password"
	When I click on the "login" button
	Then I should see "congrats" is "Wecome!"