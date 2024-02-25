import random
def guess_the_number():
    user_number = int(input("Enter your number: "))
    low = 1
    high = 100
    attempts = 0
    while True:
        guess = random.randint(low, high)
        attempts += 1
        print(f"The computer guesses: {guess}")
        if guess == user_number:
            print(f"The computer guessed your number ({user_number}) correctly in {attempts} attempts!")
            break
        elif guess < user_number:
            print("Too low!")
            low = guess + 1
        else:
            print("Too high!")
            high = guess - 1
guess_the_number()