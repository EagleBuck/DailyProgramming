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
    runner()


def runner():
    phrase = input("Input a string:\n").lower()
    guess = randomString(len(phrase))
    generation = 0
    while(True):
        generation = generation + 1
        errorList = findError(phrase, guess)
        error = sum(errorList)
        if error == 0:
            print("Done!\nGen: " + str(generation) + "; In: " + phrase)
            runner()
        else:
            print(guess + " - G: " + str(generation) + "; E: " + str(error))
            guess = guessAdjust(guess, errorList)

def guessAdjust(guess, errorList):
    newGuess = list(guess)
    position = 0
    print(errorList)
    while position < len(newGuess):
        if errorList[position] == 1:
            newGuess[position] = randomLetter()
        else:
            pass
        position = position + 1
    return "".join(newGuess)
    

def findError(phrase, guess):
    errorList = []
    for position in range(len(phrase)):
        if(phrase[position] != guess[position]):
            errorList.append(1)
        else:
            errorList.append(0)
    return errorList

def randomString(length):
    randString = ""
    for char in range(length):
        randString = randString + randomLetter()
    return randString

def randomLetter():
    letters = ("abcdefghijklmnopqrstuvwxyz")
    return random.choice(letters)


start()
