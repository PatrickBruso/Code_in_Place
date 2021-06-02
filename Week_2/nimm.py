"""
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called
Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:
    1. The game starts with a pile of 20 stones between the players.
    2. The two players alternate turns.
    3. On a given turn, a player may take either 1 or 2 stone from the center pile.
    4. The two players continue until the center pile has run out of stones.

The last player to take a stone loses.
"""


def main():
    stones = 20
    turns = 0
    while stones > 0:
        print(f"\nThere are {stones} stones left")
        if turns % 2 == 0:
            stones_remove = take_stone(1)
        else:
            stones_remove = take_stone(2)
        stones -= stones_remove
        turns += 1

    if turns %2 == 0:
        print("\nPlayer 1 wins!")
    else:
        print("\nPlayer 2 wins")


def take_stone(x):
    stone_choice = int(input(f"Player {x} would you like to remove 1 or 2 stones? "))

    while stone_choice != 1 and stone_choice != 2:
        stone_choice = int(input("Please enter 1 or 2: "))

    return stone_choice


if __name__ == '__main__':
    main()
