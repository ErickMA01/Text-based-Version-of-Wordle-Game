
#######################################################
# wordle_engine_tests 
#
# Name: Erick Anangwe
# Section: 03
#
# Fall 2023
#########################################################

import unittest
import wordle_engine

class wc:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class WordleEngineTest(unittest.TestCase):

#
# create_letter_status
#

    # This is the only test you need for this function
    def test_create_letter_status_01(self):
        observed = wordle_engine.create_letter_status()
        for l in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(wc.BLUE, observed[l])

#
# load_words
# 
    def test_load_words_01(self):
        observed = wordle_engine.load_words("sample_word_list.txt")
        expected = {"dog", "cat", "turkey", "sheep", "goat"}
        self.assertEqual(expected, observed)

    def test_load_words_02(self):
        observed = wordle_engine.load_words("sample_word_list1.txt")
        expected = {"start", "here", "then", "finally", "finish"}
        self.assertEqual(expected, observed)



    # Create one more test case that loads a different, short file.

#
# format_guess
#
    def test_format_guess_00(self):
        # make sure string ends with ENDC
        observed = wordle_engine.format_guess('abcde', 'fghij')
        self.assertTrue(observed.endswith(wc.ENDC), "formatted guess should end with the ENDC special character.")

    def test_format_guess_01(self):
        # no matching letters
        observed = wordle_engine.format_guess('abcde', 'fghij')
        expected = f"{wc.RED}f{wc.RED}g{wc.RED}h{wc.RED}i{wc.RED}j{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_02(self):
        # matching letter in wrong position
        observed = wordle_engine.format_guess('abcde', 'fghbj')
        expected = f"{wc.RED}f{wc.RED}g{wc.RED}h{wc.YELLOW}b{wc.RED}j{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_03(self):
        # matching letter in right position
        observed = wordle_engine.format_guess('abcde', 'fgcbj')
        expected = f"{wc.RED}f{wc.RED}g{wc.GREEN}c{wc.YELLOW}b{wc.RED}j{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_04(self):
        # multiple matching letters in wrong positions
        observed = wordle_engine.format_guess('abcde', 'fabjc')
        expected = f"{wc.RED}f{wc.YELLOW}a{wc.YELLOW}b{wc.RED}j{wc.YELLOW}c{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_05(self):
        # one in right position, multiple matching letters in wrong positions
        observed = wordle_engine.format_guess('abcde', 'fabdc')
        expected = f"{wc.RED}f{wc.YELLOW}a{wc.YELLOW}b{wc.GREEN}d{wc.YELLOW}c{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_06(self):
        # one in right position, one in wrong position, rest not matching
        observed = wordle_engine.format_guess('abcde', 'fbhaj')
        expected = f"{wc.RED}f{wc.GREEN}b{wc.RED}h{wc.YELLOW}a{wc.RED}j{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_07(self):
        # all letters match
        observed = wordle_engine.format_guess('abcde', 'abcde')
        expected = f"{wc.GREEN}a{wc.GREEN}b{wc.GREEN}c{wc.GREEN}d{wc.GREEN}e{wc.ENDC}"
        self.assertEqual(expected, observed)

    def test_format_guess_08(self):
        # double letters
        observed = wordle_engine.format_guess('abcab', 'abcab')
        expected = f"{wc.GREEN}a{wc.GREEN}b{wc.GREEN}c{wc.GREEN}a{wc.GREEN}b{wc.ENDC}"
        self.assertEqual(expected, observed)

    # Write several more test cases to make sure different color combinations are handled correctly.
    # Don't forget about double letters.

#
# update_letter_status
#

    def test_update_letter_status_01(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'abcde', 'abdcf')
        # individual letters check
        self.assertEqual(wc.GREEN, observed_letter_status["a"]) 
        self.assertEqual(wc.GREEN, observed_letter_status["b"]) 
        self.assertEqual(wc.YELLOW, observed_letter_status["c"]) 
        self.assertEqual(wc.YELLOW, observed_letter_status["d"]) 
        self.assertEqual(wc.BLUE, observed_letter_status["e"]) 
        self.assertEqual(wc.RED, observed_letter_status["f"]) 

        # other letters
        for l in "ghijklmnopqrstuvwxyz":
            self.assertEqual(wc.BLUE, observed_letter_status[l])

    def test_update_letter_status_02(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'abcde', 'abcde')
        # all letters used and right postion
        self.assertEqual(wc.GREEN, observed_letter_status["a"])
        self.assertEqual(wc.GREEN, observed_letter_status["b"])
        self.assertEqual(wc.GREEN, observed_letter_status["c"])
        self.assertEqual(wc.GREEN, observed_letter_status["d"])
        self.assertEqual(wc.GREEN, observed_letter_status["e"])

        # other letters
        for l in "fghijklmnopqrstuvwxyz":
            self.assertEqual(wc.BLUE, observed_letter_status[l])

    def test_update_letter_status_03(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'hello', 'world')
        # check for some letters match, some letters don't match
        self.assertEqual(wc.BLUE, observed_letter_status["h"])
        self.assertEqual(wc.BLUE, observed_letter_status["e"])
        self.assertEqual(wc.RED, observed_letter_status["w"])
        self.assertEqual(wc.YELLOW, observed_letter_status["o"])
        self.assertEqual(wc.RED, observed_letter_status["r"])
        self.assertEqual(wc.GREEN, observed_letter_status["l"])
        self.assertEqual(wc.RED, observed_letter_status["d"])

        # other letters
        for l in "abcfgijkmnpqstuvxyz":
            self.assertEqual(wc.BLUE, observed_letter_status[l])

    def test_update_letter_status_04(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'sorry', 'watch')
        # all letters don't match
        self.assertEqual(wc.BLUE, observed_letter_status["s"])
        self.assertEqual(wc.BLUE, observed_letter_status["o"])
        self.assertEqual(wc.BLUE, observed_letter_status["r"])
        self.assertEqual(wc.BLUE, observed_letter_status["y"])
        self.assertEqual(wc.RED, observed_letter_status["w"])
        self.assertEqual(wc.RED, observed_letter_status["a"])
        self.assertEqual(wc.RED, observed_letter_status["t"])
        self.assertEqual(wc.RED, observed_letter_status["c"])
        self.assertEqual(wc.RED, observed_letter_status["h"])

        # other letters
        for l in "bdefgijklmnpquvxz":
            self.assertEqual(wc.BLUE, observed_letter_status[l])

    def test_update_letter_status_05(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'apple', 'sapel')
        # individual letters check
        self.assertEqual(wc.YELLOW, observed_letter_status["a"])
        self.assertEqual(wc.GREEN, observed_letter_status["p"])
        self.assertEqual(wc.RED, observed_letter_status["s"])
        self.assertEqual(wc.YELLOW, observed_letter_status["l"])
        self.assertEqual(wc.YELLOW, observed_letter_status["e"])

        # other letters
        for l in "bcdfghijkmnoqrtuvwxyz":
            self.assertEqual(wc.BLUE, observed_letter_status[l])


    # Write several more test cases to make sure different color combinations are handled correctly.
    # Don't forget about double letters.

    #    

#
# format_letters
#

    # These are the only tests you need for this function

    def test_format_letters_00(self):
        # Make sure string ends with ENDC
        letter_status = wordle_engine.create_letter_status()
        observed = wordle_engine.format_letters(letter_status)
        self.assertTrue(observed.endswith(wc.ENDC), 
                        "formatted letters should end with the ENDC special character.")

    def test_format_letters_01(self):
        letter_status = wordle_engine.create_letter_status()
        letter_status["b"] = wc.GREEN
        letter_status["f"] = wc.RED
        letter_status["q"] = wc.YELLOW

        expected = [] 
        for l in "abcdefghijklmnopqrstuvwxyz":    
            if l == "b":
                expected.append(f"{wc.GREEN}b")
            elif l == "f":
                expected.append(f"{wc.RED}f")
            elif l == "q":
                expected.append(f"{wc.YELLOW}q")
            else:
                expected.append(f"{wc.BLUE}{l}")

        expected.append(wc.ENDC)
        self.assertEqual("".join(expected), wordle_engine.format_letters(letter_status) )

# This bit of "magic" lets you run the tests from the command line by 
# running "python wordle_engine_test.py"


if __name__ == '__main__':
    unittest.main()
