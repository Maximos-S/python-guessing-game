import random

RANDOM_NUM = random.randint(1, 100)

NAME = input("Hello what is your name?")

print(f"Well, {NAME}, I am thinking of a number between 1 and 100")

GUESS = None

while GUESS != RANDOM_NUM:
    GUESS = int(input("Take a guess"))
    if (GUESS < RANDOM_NUM):
        print("Your guess is too low")
    if (GUESS > RANDOM_NUM):
        print("Your guess is too high")

print("Congrats!")
