import random

number = random.randint(1, 10)

guess = input("Type your lucky number" + " ")
guess = int(guess)

if guess == number:
    print("Well done boy")
else:
    print("wrong")
