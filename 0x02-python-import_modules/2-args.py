#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    c = ':'
    if length == 0:
        c = 's.'
    if length => 1:
        c = 's:'
    print("{} argument{}".format(length, c))
    for i in range(1, length + 1):
        print("{} : {}".format(i, argv[i]))
