"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

SENTINEL = -1


def main():
    return_sum = 0
    number = int(input("Enter a number: "))

    while number != SENTINEL:
        return_sum += number
        number = int(input("Enter a number: "))

    print(return_sum)


if __name__ == '__main__':
    main()
