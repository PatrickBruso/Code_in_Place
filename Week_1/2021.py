from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    """
    Program to create the year '2021' by placing 20 beepers,
    moving right, placing 21 beepers, then moving right again.
    """
    for i in range(20):
        put_beeper()

    move()

    for i in range(21):
        put_beeper()

    move()

if __name__ == '__main__':
    run_karel_program('3x3.w')