"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random

# constants
MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print(f"What is {num1} + {num2}?")
    answer = float(input("Your answer: "))
    if answer == num1 + num2:
        print("Correct!")
    else:
        print(f"Incorrect. The expected answer is {num1 + num2}")


if __name__ == '__main__':
    main()
