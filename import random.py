import random
import pandas as pd
die_rolls = [0] * 6 

roll = random.randint(1,6)
die_rolls[roll - 1] += 1
print(die_rolls)

die_roll = {"One" : die_rolls[0],
             "Two" : die_rolls[1],
             "Three" : die_rolls[2],
             "Four" : die_rolls[3],
             "Five" : die_rolls[4],
             "Six" : die_rolls[5]}
print(die_roll)

dierolls = {"Number" : list(die_roll.keys()),
              "rolls" : list(die_roll.values())}
fruit_df = pd.DataFrame.from_dict(dierolls)
fruit_df