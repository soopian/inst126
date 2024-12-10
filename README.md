 Tuple Out Game

 Overview

Tuple Out is a dice game where the player rolls three dice and attempts to match the numbers on all dice to "tuple out". 
The game allows multiple rounds, and the goal is to score as high as possible by adding the sum of dice rolls. 
If the player rolls the same number on all three dice, they "tuple out" and the round ends. 
The player can also choose to reroll specific dice.

 Features

- Roll Dice: Simulates rolling three six-sided dice.
- Tuple Out: A condition where the player rolls the same number on all three dice.
- Reroll Dice: The player can choose to reroll one or more dice each round.
- High Score: The game tracks the highest score across multiple games.
- Multiple Rounds: The game allows the player to choose how many rounds to play.

 How to Play

1. Start the Game: The game asks how many rounds you want to play.
2. Rolling Dice: In each round, three dice are rolled. The dice values are displayed.
3. Reroll Dice: You can choose to reroll any die. The game will inform you if you cannot reroll a particular die (if it is "fixed").
4. Tuple Out: If all three dice show the same number, you "tuple out", and the round ends. The score for that round is the sum of the dice.
5. High Score: After finishing the rounds, the game displays your total score. If you beat the high score, it will be updated.

Instructions

How to Play:
Input the number of rounds you'd like to play when prompted.
After the dice are rolled, choose which dice to reroll (if any).
If all three dice are the same, you "tuple out", and the round ends.
Continue rerolling or finishing the round until you decide to stop.

Commands:

y/n: Used to indicate if you want to reroll dice or play another game.
Choose Dice: You can select which dice to reroll by inputting the corresponding number (1, 2, or 3).

 Code Breakdown

Functions

rolldice(): Simulates the roll of a single die, returning a random number between 1 and 6.

checktuple(dice): Checks if the player has "tupled out" by comparing if all dice have the same value.

checkfixed(dice): Checks which dice are "fixed" (those that match with another die) and cannot be rerolled.

playgame(): A function that simulates one round of the game, rolls the dice, handles rerolling, and calculates the score for that round.

 Main Game Loop

- rounds: The number of rounds the player wants to play.
- Highscore: Tracks the highest score achieved across multiple games.
- Replay: After each game, you can choose whether to play again or not.

 Example Game Flow

```
How many rounds do you want to play? 3
[5, 2, 4]
Do you want to reroll any of your dice? y/n y
Which die do you want to roll? 1
[3, 2, 4]
Do you want to reroll any of your dice? y/n n
final roll for this round:
[3, 2, 4]
Score for this round: 9
...

Do you want to play again? y/n n
```



