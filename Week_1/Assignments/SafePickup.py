from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""

def main():
    """
    This program is fairly self-explanatory.  If there is a beeper on the current position,
    Karel should pick it up.  Otherwise, Karel should do nothing.
    """
    if beepers_present():
        pick_beeper()

if __name__ == '__main__':
    run_karel_program('SafePickup2.w')