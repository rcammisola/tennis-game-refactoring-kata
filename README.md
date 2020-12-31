# Tennis Game - Refactoring

Based on code from Emily Bache's repository
https://github.com/emilybache/Tennis-Refactoring-Kata

## Scenario

Imagine you work for a consultancy company, and one of your colleagues has been doing some work for the Tennis Society. 
The contract is for 10 hours billable work, and your colleague has spent 8.5 hours working on it. 
Unfortunately he has now fallen ill. He says he has completed the work, and the tests all pass. 
Your boss has asked you to take over from him. She wants you to spend an hour or so on the code so she can bill the client for the full 10 hours. 
She instructs you to tidy up the code a little and perhaps make some notes so you can give your colleague some feedback on his chosen design. 
You should also prepare to talk to your boss about the value of this refactoring work, over and above the extra billable hours.

There are three versions of this refactoring kata, each with their own design smells and challenges. 
I suggest you start with the first one, with the class "TennisGame1". The test suite provided is fairly comprehensive, and fast to run. 
You should not need to change the tests, only run them often as you refactor.

## Initial run

* Flat repository
* pytest run with coverage `make test`
* 97% Covered
    * Unused methods in TennisGame2 that SetP1Score and SetP2Score

### How do the tests run?

* Tests run through the test cases in `tennis_unittest.py` and runs them through the play_game harness. 
* Harness is called with the game runner class, the final score and the player names.
* play_score sets the game to the correct state and returns the game object


## Tennis Game 1

### Code Smells?

1. Style clutter
    1. naming style is not pythonic - should use snake case instead of camel case
    1. if clauses have unnecessary parentheses
1. Dead code
    1. line 19 variable tempScore initialised but completely unused until the in progress game score branch (L37 onwards)  

1. Ongoing game score creation is using unnecessary looping and unclear as to how it's working
    1. Extract method to get player points category / string
    1. Simplify loop to just pull the category for each player's current score and build a score string
