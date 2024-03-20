# Text-based-Version-of-Wordle-Game
## CIS 500 Project 2

For this project, you are going to implement a text-based version of Wordle that produces colored output.

The goals of the project are to:

* Practice writing Python code using loops, dictionaries, sets, and file I/O.
* Practice writing unit tests for functions.
* Practice writing end-to-end tests
## Prerequisites
* Learn how to play Wordle. (This video may be helpful.)
* Watch this demo of the program you will be creating.
## Color output
Your program will produce colored output. In order to change the color of text output, you need only add a special character sequence to your output string. These special sequences are provided in the starter code. For example, to print the string "I hate hard projects" with the word "hate" in Red, you would do this:

`print(f"I {wordle_color.RED}hate{wordle_color.ENDC} hard projects.")`

The variable `wordle_color.RED` contains the character sequence that causes the following characters to appear red. The variable `wordle_color.ENDC` contains the character sequence that returns the output to normal.

(If you are curious, these "special character sequences" are ANSI escape codes.)

## Instructions
Step 1: Begin by examining the function `wordle_engine.welcome_string()` to see how to use colors. Practice using the `wordle_colors` class by adding a line or two to the welcome message. (You may add additional colors to the class if you like; but, you must follow the specifications when displaying guesses and letter options.)

As with Project 1, designing and writing tests is an important component. In order to facilitate some automated testing, you must implement and use the functions in `wordle_engine.py` as documented. (In other words, implement the functions as described. Don't give them different behavior, and don't modify their parameters or return values.)

Step 2: Next, add test cases to `wordle_engine_tests.py`. Be sure to read the comments in the test file. They will give you an idea of how many additional tests to write.

Step 3: Now, write end-to-end tests. The tests in `wordle_engine_tests.py` are what we call unit tests. They only test a single unit of code (in this case a function). Because you are writing a complete program, you also need some end-to-end tests which test the program as a whole. Although it is possible to automate end-to-end tests, we won't for this project. Instead, you need only edit `end_to_end.txt` to make a list of the different scenarios that should be tested before submitting your program.

Step 4: Once you have written your tests, implement the code in `wordle_engine.py` and debug it until it passes your tests.

Step 5: Now, write the main game loop in `wordle.py`.

You must implement the code in `wordle_engine.py` so that it passes the instructor's tests. Also, your game must do the following:

* Reject guesses that are not exactly 5 letters
* Reject guesses that are not valid words
* Limit players to 6 guesses
* Display the entire history of guesses before each prompt.
* Print a message at the end of the game indicating whether the player won or lost.
  * If the player wins, display the entire sequence of guesses as part of the final message.
Other than that, you have freedom to design the game how you like.

The starter code comes with two files

* `combined_wordlist.txt` This is the set of all acceptable guesses.
* `shuffled_real_wordles.txt` This much shorter list is the set of potential "target" words.
The target word is chosen in one of two ways:

* Specify it on the command line
* Choose it randomly from the list of all acceptable guesses (You must add code to implement this.)
Instead of choosing the target from the list of all words, you can choose it randomly from `shuffled_real_wordles.txt`. (This option requires a little extra work on your part to open and load this extra file.)

On Mac and Linux (and maybe Windows?) there is a way to choose a target word from `shuffled_real_wordles.txt` without adding extra code to your project. You can run your wordle program from the command line using this command:

python3 wordle.py `sort -R shuffled_real_wordles.txt | head -1`
**IMPORTANT**: Be sure to test your entire program thoroughly. Automated tests cover only a small portion of this assignment. Simply passing the automated tests does not mean that your project is complete.
