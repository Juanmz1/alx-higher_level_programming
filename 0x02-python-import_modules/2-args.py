#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length_1 = len(argv) - 1
    c = ':'
    if length_1 == 0:
        c = 's.'
    if length_1 > 1:
        c = 's:'
    print("{} argument{}".format(length_1, c))
    for i in range(1, length_1 + 1):
        print("{}: {}".format(i, argv[i]))
