import random
from random import randint

    #Player gets 5 tries
tries = 0

    # Welcome people to the game by asking their name.
print("Hello, and welcome. May I have your name?")
name = input()
    
    # Ask if they want to play a guessing game
print(f"Hello {name}, this is a guessing game. I think of a number and you have 5 tries to guess.\n\n")

    #Computer picks a random number in range of 1-20
randomNumber = randint(1, 20)

    # Start the game. 
print(f"Let us begin, goodluck.\n\n"f"I am thinking of a number between 1 and 20")

    # Conditionals
while tries < 5:
    print("What number do you choose?: ")
    guess = input()
    guess = int(guess)
    tries = tries + 1
    if guess > randomNumber + 3:
        print("That is too high")
    elif guess < randomNumber - 3:
        print("That is too low")
    elif guess > randomNumber:
        print("Close! A little lower")
    elif guess < randomNumber:
        print("Close! A little higher")
    elif guess == randomNumber:
        break
    
    #Exit loop conditional.
if guess == randomNumber:
        print("You win!")
        print(f"The random number was {randomNumber}")
        print(f"It took you {tries} tries!")

if guess != randomNumber:
    print("The computer wins!")
    
    