from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    Program to have Karel draw a diagonal line across an odd columned
    world placing a beeper to create a slope of 1/2.
    """
    put_beeper()
    while front_is_clear():
        draw_line()

def draw_line():
    move()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')