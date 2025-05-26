import random

number = random.randint(0, 100)
guess = int(input("Guess a number: "))


while number != guess:
    if guess < number:
        print("Guess too low")
        guess = int(input("Guess another number: "))
    if guess > number:
            print("Guess too high")
            guess = int(input("Guess another number: "))
    else:
         break
print("You guessed the number correct!")
         