"""Bagels game by Filip Szymanski
Practice coding game"""

import random

MAX_DIGITS = 3
MAX_TRIES = 10

def main():
    """Main loop of program"""

    print(f'''This is a guess a {MAX_DIGITS} digit game.  You have {MAX_TRIES} tries.  012 is a valid number.

When I say:   That means:
Pico          One digit is correct but in the wrong position.
Fermi         One digit is correct and in the right position.
Bagels        No digit is correct.\n\n''')

    guessTry = 1
    mainLoop = True

    secretNumber = generateNumber()
    # print('Secret: ' + secretNumber)

    while(mainLoop):
        """Main game loop.  Capture user's guess and compare until match or number of tries is maxed out"""
        guess = input(f'Guess #{guessTry} > ')
        print(str(compareNumbers(guess, secretNumber)) + '\n')


        # print(guess)
        guessTry += 1
        if guessTry > MAX_TRIES:
            print('You are out of guesses, game over')
            mainLoop = False

def generateNumber():
    """Generate a random number consisting of MAX_DIGITS"""

    number = ''
    for i in range(MAX_DIGITS):
        number += str(random.randint(0, 9))
    return number

def compareNumbers(guess, secretNumber):
    """Compare user's guess with secret number and print one of the following:
    Pico          For each digit that is correct but in the wrong position.
    Fermi         For each digit that is correct and in the right position.
    Bagels        No digit is correct"""

    if guess == secretNumber:
        print('You guessed the number right!')
        exit()

    success = []
    for i in range(MAX_DIGITS):
        if guess[i] == secretNumber[i]:
            success += ['Fermi']
        elif guess[i] in secretNumber:
            success += ['Pico']
    
    if len(success) == 0:
        return 'Bagels'

    success.sort()
    return ' '.join(success)

if __name__ == '__main__':
    main()