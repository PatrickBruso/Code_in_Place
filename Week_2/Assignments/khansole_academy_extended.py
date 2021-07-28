"""
Prints out randomly generated addition problems until user answers three problems correctly
in a row, then exits.
"""

import random

# constants
MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    streak_num = 0  # set streak to 0 to calculate correct answers in a row

    while streak_num < 3:  # quit after three correct in a row
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)

        print(f"What is {num1} + {num2}?")
        answer = float(input("Your answer: "))

        if answer == num1 + num2:
            streak_num += 1  # increase streak number for correct answer
            print(f"Correct! You've gotten {streak_num} correct in a row.")
            if streak_num == 3:  # if three correct in a row print congrats.
                print("Congratulations! You mastered addition.")
        else:
            print(f"Incorrect. The expected answer is {num1 + num2}")
            streak_num = 0  # reset streak number to 0 upon wrong answer


if __name__ == '__main__':
    main()
