import random

number = random.randint(1,10)

guess_limit = 5


for limit in range(guess_limit):
    guess = int(input("Guess a number from 1-10: "))

    if guess == number:
        print("You Win!")
        exit()


print("You lose!")
