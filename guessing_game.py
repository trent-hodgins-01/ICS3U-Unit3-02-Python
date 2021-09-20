# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/17/20
# This is a guessing game program
# The user enters in a number between 1 and 9

import constants


def main():
    # this function checks to see if the user guessed the correct number(5)

    # input
    guessed_number = int(input("Guess a number between 0 and 9 (integer): "))
    print("")

    # process and output
    if constants.CORRECT_NUMBER == guessed_number:
        print("You Guessed Correctly")
        print("")
        print("Done.")
    else:
        print("You Guessed Wrong!")
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
