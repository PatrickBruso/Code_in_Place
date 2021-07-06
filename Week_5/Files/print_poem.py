"""
Program that opens a text file and prints each line
"""

# version 1
f = open("invictus.txt")  # open file in program
for line in f:  # iterate through text in file
    print(line)
f.close()  # close the text file

# version 2
f = open("invictus.txt")
for line in f:
    # we could alternatively use .strip() or .strip("\n") here
    line = line.rstrip()  # get rid of empty lines
    print(line)
f.close()

# version 3
with open("invictus.txt") as f:  # creates f for us and automatically closes it when file has been read by program
    for line in f:
        print(line.rstrip())
