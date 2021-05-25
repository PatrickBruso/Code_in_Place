from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    Program to pick up a puzzle piece, place the piece in the appropriate
    position, and move back to the starting position. This program uses
    functions for each step.
    """
    pickup_piece()
    place_piece()
    return_to_position()

def pickup_piece():
    move()
    move()
    pick_beeper()

def place_piece():
    move()
    turn_left()
    move()
    move()
    put_beeper()

def return_to_position():
    turn_left()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
