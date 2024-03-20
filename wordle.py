
#######################################################
# wordle
#
# Name: Erick Anangwe
# Section: 03
#
# Fall 2023
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import random
import sys

# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")

# Use the target word provided on the command line, 
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # TODO choose a random word from valid_words
    target = random.choice(list(valid_words))

#print(target)

# TODO Implement the rest of the game.
# Remember:

#   * Guesses must be exactly 5 letters
#   * Guesses must be valid words
#   * Players get at most 6 guesses
#   * Please display the entire history of guesses before each prompt.
#   * Add color functionalities using format_letters, update_letter_status, format_guess functions
#   * Print a message at the end of the game indicating whether the player won or lost.
#   * If the player wins, display the entire sequence of guesses as part of the final message.

# variables for the game
guesses = []
max_guesses = 6
letter_status = wordle_engine.create_letter_status()

# game loop
while max_guesses > 0:
    # display the history of guesses
    if guesses:
        print("Guess history:")
        for i, guess in enumerate(guesses, start=1):
            print(f"Guess {i}: {wordle_engine.format_guess(target, guess)}")
        print(wordle_engine.format_letters(letter_status))

    # prompting the player for a guess
    player_guess = input(f"Enter a 5-letter word guess ({max_guesses} guess(es) left): ").strip().lower()

    # validating the guess to see if it meets requirements
    if len(player_guess) != 5:
        print("Your guess must be exactly 5 letters.")
        continue

    if player_guess not in valid_words:
        print("Your guess is not a valid word.")
        continue

    # add the guess to the history
    guesses.append(player_guess)

    # update letter status
    letter_status = wordle_engine.update_letter_status(letter_status, target, player_guess)

    # check if a win
    if player_guess == target:
        print("Guess history:")
        for i, guess in enumerate(guesses, start=1):
            print(f"Guess {i}: {wordle_engine.format_guess(target, guess)}")
        print(wordle_engine.format_letters(letter_status))
        print("Congratulations! You won! Target word was:", target)
        break

    # decrease remaining guesses after each guess
    max_guesses -= 1

# game ends when there are no more guesses left
if max_guesses == 0:
    print("Your guesses are over. Target word was:", target)
