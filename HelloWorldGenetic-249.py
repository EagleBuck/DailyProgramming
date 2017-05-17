import random

# 2017-05-17
# Task #2
# Challenge #249, published 2016-01-13
# Hello World Genetic


'''
The input string should be the target string you want to evolve the initial
random solution into.
The target string (and therefore input) will be
'Hello, world!'
However, you want your program to initialize the process by randomly generating
a string of the same length as the input. The only thing you want to use the
input for is to determine the fitness of your function, so you don't want to
just cheat by printing out the input string!
Output description

The ideal output of the program will be the evolutions of the population until
the program reaches 'Hello, world!' (if your algorithm works correctly). You
want your algorithm to be able to turn the random string from the initial
generation to the output phrase as quickly as possible!
'''


def start():
    print("This program will evolve its output text until it matches the input text")
    kickoff()

def kickoff():
    phrase = input("Input a string:\n")
    guess = randomString(len(phrase)).lower()
    runner(phrase, guess)

def runner(phrase, guess):
    error = findError(phrase, guess)
    if error == 0:
        print("Done!")
        kickoff()
    else:
        guess = randomString(len(phrase))
        runner(phrase, guess)

def findError(phrase, guess):
    error = 0
    for position in range(len(phrase)):
        if(phrase[position] != guess[position]):
            error = error + 1
        else:
            pass
    print("Errors: " + str(error))
    return error

def randomString(length):
    letters = ("abcdefghijklmnopqrstuvwxyz")
    randString = ""
    for char in range(length):
        randString = randString + random.choice(letters)
    print(randString)
    return randString


start()
