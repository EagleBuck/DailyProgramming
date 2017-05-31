
# Kaprekar Numbers
# Started 2017-05-22

# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/

'''
In mathematics, a Kaprekar number for a given base that is a non-negative integer,
the representation of whose square in that base can be split into two parts that
add up to the original number again. For instance, 45 is a Kaprekar number,
because 45^2 = 2025 and 20+25 = 45. The Kaprekar numbers are named after
D. R. Kaprekar.
I was introduced to this after the recent Kaprekar constant challenge.
For the main challenge we'll only focus on base 10 numbers. For a bonus, see if
you can make it work in arbitrary bases.
'''


def start():
    while(True):
        userIn = input("Input 2 digit number:\n")
        if(len(userIn) == 2):
            digitOne = str(userIn)[0]
            print(digitOne)
            digitTwo = str(userIn)[1]
            isKaprekar(digitOne, digitTwo)
        else:
            pass
        
    

def isKaprekar(digitOne, digitTwo):
    



start()
