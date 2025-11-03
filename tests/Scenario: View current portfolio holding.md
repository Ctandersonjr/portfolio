Scenario: View current portfolio holdings
Given: A logged in user with an active account
And: The user has existing portfolio holdings
When: The user views their portfolio
Then: The user sees a list of their current holdings with details such as quantity, purchase price, and current market value.

Scenario: User can add  holdings
Given: The user correctly logs in
When: The user inserts a valid holding
Then: The user can make the choice to add holding

Scenario: User can delete holdings
Given: The user correctly logs in
When: The user selects a previously saved holding to delete
Then: The user can make the choice to delete holding

Scenario: User can view graphical visualizations for the following data: historical stock price, portfolio gains and losses, and portfolio risks.
Given: A logged in user has holdings 
When: A user select a graphical view
Then: The user sees visualizations for the historical stock price, portfolio gains and losses, and portfolio risks.

Scenario: User can have access to a IRS form tax Data
Given: The logged in user has securities purchased and gained a profit
When: The logged in user selects a link to the IRS form
Then: The user will have a record of purchased securities for Tax data. 