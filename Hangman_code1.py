import random

# 1. List of words
words = ["apple", "banana", "grapes", "mango", "orange"]

# 2. Choose a random word
word = random.choice(words)

# 3. Variables
guessed_letters = ""
attempts = 6

print("Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

# 4. Game loop
while attempts > 0:
    display_word = ""

    # Show the word with guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    # If word is fully guessed
    if display_word == word:
        print("🎉 Congratulations! You guessed the word!")
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Check the guess
    if guess in word:
        print("✅ Correct!")
        guessed_letters += guess
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

    print()

# If user runs out of attempts
if attempts == 0:
    print("💀 Game Over! The word was:", word)
