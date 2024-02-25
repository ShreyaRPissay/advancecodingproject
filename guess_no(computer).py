import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    num_guesses = 0
    while True:
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
guess_the_number()
