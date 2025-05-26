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
<<<<<<< HEAD
print("You guessed the number correct!")
=======
print("You guessed correct!")
>>>>>>> 0e2edd32c2307d6ef61a2ce0fcf6e7a9a3fbff15
         