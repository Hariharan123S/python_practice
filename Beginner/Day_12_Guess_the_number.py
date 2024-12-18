import random
import art
print(art.logo_guess)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    a = 10
    print("You have 10 attempts remaining to guess the number")
    rd = random.randint(1, 100 + 1)
    guess = int(input("Make a guess: "))
else:
    a = 5
    print("You have 5 attempts remaining to guess the number")
    rd = random.randint(1, 100 + 1)
    guess = int(input("Make a guess: "))

a = 10
b = 5
condition = True
while condition:
    if guess > rd and level == "easy":
        print("Your guess is too high")
        a -= 1
        if a == 0:
            print("You have run out of guesses, you lose.")
            condition = False
            break
        print(f"You have {a} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
    elif guess < rd and level == "easy":
        print("Your guess is too low")
        a -= 1
        if a == 0:
            print("You have run out of guesses, you lose.")
            condition = False
            break
        print(f"You have {a} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
    elif guess > rd and level == "hard":
        print("Your guess is too high")
        b -= 1
        if b == 0:
            print("You have run out of guesses, you lose.")
            condition = False
            break
        print(f"You have {b} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
    elif guess < rd and level == "hard":
        print("Your guess is too low")
        b -= 1
        if b == 0:
            print("You have run out of guesses, you lose.")
            condition = False
            break
        print(f"You have {b} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
    elif guess == rd:
        print(f"You go it! The answer was {rd}.")
        condition = False


