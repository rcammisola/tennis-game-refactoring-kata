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
    1. minus code is a poor variable name for the concept of score difference

1. Dead code
    1. line 19 variable tempScore initialised but completely unused until the in progress game score branch (L37 onwards)  

1. Ongoing game score creation is using unnecessary looping and unclear as to how it's working
    1. Extract method to get player points category / string
    1. Simplify loop to just pull the category for each player's current score and build a score string

1. Advantage and game won scenarios handled in the same clause mean there are multiple reasons for that to change
    1. Separate out Win and Advantage 
    1. this was difficult to do with automated refactorings
    1. Some steps taken
        1. Pull game over situation to the top level
        1. Create boolean helpers to determine whether game over/advantage situation is in play
        1. this made the score difference redundant
        1. reverted the tied situation check to points equality which is more intuitive check
        1. added a helper method to get the leading player and use that name to build the string rather than duplicating string building
    
1. Group together score calculation for in-progress game into a method `_in_progress_game_score` so that we have a method 
that would only change if the incomplete scoring required changes.

1. Remove magic numbers for point values - created constants for points values love, fifteen, thiry, forty. These were 
tricky to name and I'm still unsure about them 1 == 15?!

1. Modified check for game over - check if either player has MORE than Forty rather than the meaningless 4 or more

1. Modified check for advantage, check that BOTH players have Forty or more points

### Reservations about the implementation

* Concerns for calculating and representing the game score are mixed
    * If I wanted to display the score on a scoreboard and use the score for some commentary I would want to have different 
    representations of the score shown
    * e.g. "Ad" by the player in the lead compared to the "Advantage Player" provided
* Would be interesting to extend the kata further to handle multiple cases at a Tennis tournamnet
    * Scoreboard
    * JudgeBot
    * Commentator
    * Would also want to roll game results up to Set and Match scores


## Tennis Game 2

### Code Smells?

1. variable and method naming style
1. Long method
1. Dead code (SetP1Score and SetP2Score)
1. magic strings and numbers
1. Loads of duplication
1. Mixing of concerns - setting player 1 result and player 2 result jumbled together
1. Unclear what each separate if block is for
1. Unnecessary check that the opposition has 0+ points in the game over conditionals
    1. Removed

1. Removed duplication of result string for Win and Advantage branches

1. Simplify conditional to switch-like form

Before:
```
if (self.p2points > self.p1points and self.p2points < 4):
    if (self.p2points == 2):
        P2res = "Thirty"
    if (self.p2points == 3):
        P2res = "Forty"
    if (self.p1points == 1):
        P1res = "Fifteen"
    if (self.p1points == 2):
        P1res = "Thirty"
```


After:
```
if (self.p2points > self.p1points and self.p2points < 4):
    if self.p2points == 2:
        P2res = "Thirty"
    elif self.p2points == 3:
        P2res = "Forty"
    if self.p1points == 1:
        P1res = "Fifteen"
    elif self.p1points == 2:
        P1res = "Thirty"
```

* Refactoring was automated by Sourcery plugin
* Switch-like form groups related if statements into if-elif blocks rather than consecutive if that may lead to overwriting

1. Won game situation should act as a guard clause - if we're already done then just get out of the method

1. Impose switch-line setup so that ongoing game section is encapsulated

1. Simplify on-going game logic to player1-player2
    1. Now that we have the clauses re-arranged most of this code just goes away
    1. The points lookup helper is very useful here as well - there's no reason to 
    hard code a player's points in specific scenarios

1. Tied score branches rolled together

1. De-duplicate leading player lookup

1. use point constants
1. use point category name function created for game 1?
1. P1 Score and P2 Score methods are unnecessary?
1. Style changes
    1. naming cases
    1. variable name length (e.g. p1points)

1. Use methods to clarify if-clauses
    1. size of lead

1. Push advantage clause down to separate won/complete game from ongoing game
    1. Flow is now something like:
        1. Has the game ended?
        1. In-progress
            1. game tied?
            1. in an Advantage scenario?
            1. standard score

#### TODO:

1. Setup pycharm testing

### Thoughts

* Game2 is a good example of where a component accumulates technical debt with new features/bug fixes over a long period of time.
    * Multiple redundant clauses added in haste to meet a deadline without spending time refactoring
* Felt like it was possible to get quite far before trying to do any semantic refactoring (naming constants and extracting methods)
    * Think this is useful to consider where possible in order to avoid having the wrong abstraction - within reason
    * Link to Sandi Metz talk?



