import random
import time

number = random.randrange(0, 20, 1)
print("Guess the number between 0 to 20: ", end="")
guess = int(input())
atte: int = 4
guessed = 0

while atte > 0 and guessed != 1:
    if guess == number:
        guessed = 1
    else:
        if guess > number:
            print("Too high")
        else:
            print("Too low")
        print("Try again: ", end="")
        while True:
            guess = int(input())
            if -1 < guess < 21:
                break
            else:
                print("Out of range", end = "")
        atte -= 1

if guessed == 1 or number == guess:
    print("You win")
else:
    print(f"You lose and the number is: {number}")