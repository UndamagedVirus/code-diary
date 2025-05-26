import random

answer = input("Do you want to roll the dice? Y/N")

if answer == "Y":
    print("You rolled a ",random.randint(1,6))
else:
    print("Come back next time")