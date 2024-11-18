#tuple out project
import random


def rolldice():
    return random.randint(1,6)

def checktuple(dice):
    return len(set(dice)) == 1

def checkfixed(dice):
    fixeddice = [False,False,False]
    if dice[0] == dice[1]:
        fixeddice[0] = True
        fixeddice[1] = True
    if dice[0] == dice[2]:
        fixeddice[0] = True
        fixeddice[2] = True
    if dice[1] == dice[2]:
        fixeddice[1] = True
        fixeddice[2] = True
    return fixeddice
def playgame():
    die1 = rolldice()
    die2 = rolldice()
    die3 = rolldice()
    dice = [die1, die2, die3]
    print(dice)
    reroll = input("Do you want to reroll any of your dice? y/n")
    while reroll == "y":
        
        check = checkfixed(dice)
        rerolldie = int(input("Which die do you want to roll"))
        if check[rerolldie-1]:
            print("Can't roll, die is fixed")
        else:
            dice[rerolldie-1] = rolldice()


        if checktuple(dice):
            print("you tupled out!")
            return 0
        print(dice)
        reroll = input("Do you want to reroll any of your dice? y/n")  

    score = sum(dice)
    return score






rounds = int(input("How many rounds do you want to play?"))

highscore = 0
rerun = "y"
while rerun == "y": 
    playerscore = 0
    for num in range(rounds):
        playerscore += playgame()
    print(playerscore)
    if playerscore > highscore:
        print("That's a new highscore!")
        highscore = playerscore
    rerun = input("Do you want to play again? y/n")
