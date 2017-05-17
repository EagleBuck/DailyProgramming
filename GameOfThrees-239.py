
# 2017-05-17
# Task #1
# Challenge #239, published 2015-11-02
# Game of Threes

"""
https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/?utm_content=title&utm_medium=browse&utm_source=reddit&utm_name=dailyprogrammer

Back in middle school, I had a peculiar way of dealing with super boring classes. I would take my handy pocket calculator and play a "Game of Threes". Here's how you play it:
First, you mash in a random large number to start with. Then, repeatedly do the following:
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".
While the game was originally a race against myself in order to hone quick math reflexes, it also poses an opportunity for some interesting programming challenges. Today, the challenge is to create a program that "plays" the Game of Threes.
"""


def start():
    print("start")
    print("this program will take a number\nand will reduce it to 0 by")
    print("subtracting and dividing by 3")
    kickoff()

def kickoff():
    var = int(input("Submit a number greater than 1:\n"))
    runner(var)

def runner(var):
    if(var == 1):
        print("Done!")
        kickoff()
    elif(var % 3 == 0):
        varX = var / 3
        print(str(varX) + " = " + str(var) + " / 3")
        runner(varX)
    else:
        varX = var - 1
        print(str(varX) + " = " + str(var) + " - 1")
        runner(varX)

start()
