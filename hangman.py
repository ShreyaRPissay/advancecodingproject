import random
def choose_word():
    words = ["python", "hangman", "program", "computer", "game", "coding"]
    return random.choice(words)
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(display)
        if '_' not in display:
            print("Congratulations! You've guessed the word correctly!")
            break
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            attempts -= 1
            print("Incorrect guess. Try again.")
            print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)
hangman()
