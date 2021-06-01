from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    Program to build arches starting at the first column and continuing
    every four columns until a wall is reached.
    """
    while front_is_clear():
        build_column()
        reset_to_bottom()
        move_to_next()
    build_column()

def build_column():
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if no_beepers_present():
        put_beeper()

def reset_to_bottom():
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_left()

def move_to_next():
    for i in range(4):
        move()

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')