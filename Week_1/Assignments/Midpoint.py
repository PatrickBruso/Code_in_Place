from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def main():
        create_line()
        reset_to_bottom()
        find_middle()
        move_to_bottom()
        turn_right()
        put_beeper()
        while front_is_clear():
            move()
        remove_line()
        reset_to_bottom()
        move_to_middle()

def move_to_middle():
    turn_right()
    while no_beepers_present():
        move()

def find_middle():
    turn_right()
    while no_beepers_present():
        move()
        turn_right()
        move()
        turn_left()

def create_line():
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
    put_beeper()

def remove_line():
    turn_left()
    turn_left()
    while front_is_clear():
        pick_beeper()
        move()
        turn_left()
        move()
        turn_right()
    pick_beeper()

def reset_to_bottom():
    turn_right()
    while front_is_clear():
        move()

def move_to_bottom():
    turn_left()
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint2.w')