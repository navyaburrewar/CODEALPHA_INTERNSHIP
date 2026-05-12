


import random

words = ["java", "banana", "dogs", "tiger", "space"]

chosen_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6


print("-----Welcome to Hangman Game------")


while incorrect_guesses < max_guesses:

    display_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    if guess in chosen_word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Remaining guesses:", max_guesses - incorrect_guesses)

if incorrect_guesses == max_guesses:
    print("\nYou lost!")
    print("The word was:", chosen_word)