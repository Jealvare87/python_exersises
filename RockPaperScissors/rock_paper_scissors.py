import os
import random
from typing import List

won: List[int] = [0, 0]
hand = [0, 0]
posib = ["Rock", "Paper", "Scissors"]
MAX = 3

while won[0] < 3 and won[1] < 3:
    hand[0] = random.randrange(0, 2, 1)
    print("Select between Rock[0], Paper[1], Scissors[2]: ", end="")
    while True:
        hand[1] = int(input())
        if -1 < hand[1] < 3:
            break
        else:
            print("Out of range")
    # Game Logic
    print(f"The machine has chosen {posib[hand[0]]} and you {posib[hand[1]]}")
    if (hand[0] == 0 and hand[1] == 2) or hand[0] > hand[1]:
        print("Machine has won")
    elif (hand[1] == 0 and hand[0] == 2) or hand[1] > hand[0]:
        print("You win")
    else:
        print("Tie", end="\n")
    os.system("pause")
