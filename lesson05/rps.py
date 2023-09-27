import sys
import random
from enum import Enum


"""
This is a simple Rock, Paper, Scissors game.
"""

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")  #  randomly select 1, 2, or 3

computer = int(computerchoice)

# different ways to get Enum values and names
# print(RPS(2))  --> the output is RPS.PAPER
# print(RPS.ROCK) --> the output is RPS.ROCK
# print(RPS['ROCK']) --> the output is RPS.ROCK
# print(RPS['ROCK'].value) --> the output is 1

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
