#######################################################
# wordle_engine
#
# Name: Erick Anangwe
# Section: 03
#
# Fall 2023
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"


def welcome_string():
    return f"Welcome to my {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r{wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"


def create_letter_status():
    """ Return a new dictionary that maps each letter to 
        wordle_colors.BLUE """
    letter_status = {}
    for letter in wordle_alphabet:
        letter_status[letter] = wordle_colors.BLUE
    return letter_status


def load_words(filename: str):
    """ Load the words from the specified file and place them 
        in a set. 
        Ignore any lines that begin with "#"
        """
    words = set()
    with open(filename, 'r') as wordlist:
        for line in wordlist:
            line = line.strip()
            if line and not line.startswith("#"):
                words.add(line)
        return words


def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored 
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word, 
                  but in a different location.
        * RED:    The letter does not appear in the target word 
        Also, the string should end with wordle_colors.ENDC """

    formatted_guess = ""
    for i in range(min(len(target), len(guess))):
        if guess[i] == target[i]:
            formatted_guess += f"{wordle_colors.GREEN}{guess[i]}"
        elif guess[i] in target:
            formatted_guess += f"{wordle_colors.YELLOW}{guess[i]}"
        else:
            formatted_guess += f"{wordle_colors.RED}{guess[i]}"

    formatted_guess += wordle_colors.ENDC

    return formatted_guess


def update_letter_status(letter_status, target, guess):
    """ Update the letter status dictionary to show which letters 
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""

   # for letter in letter_status:
    #    letter_status[letter] = wordle_colors.BLUE

    for i in range(len(guess)):
        if guess[i] == target[i]:
            letter_status[guess[i]] = wordle_colors.GREEN
        elif guess[i] in target:
            if letter_status[guess[i]] != wordle_colors.GREEN:
                letter_status[guess[i]] = wordle_colors.YELLOW
        elif letter_status[guess[i]] != wordle_colors.GREEN:
            letter_status[guess[i]] = wordle_colors.RED

    return letter_status


def format_letters(letter_status):
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """

    formatted_letters = ""
    for letter in sorted(letter_status.keys()):
        formatted_letters += f"{letter_status[letter]}{letter}"
    return formatted_letters + wordle_colors.ENDC

