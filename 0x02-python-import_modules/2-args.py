#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        a = '.'
        print("{} argument{}".format(length, a))
    elif argv => 1:
        a = 's:'
        print("{} argument{}".format(length, a))
    for i in range(length):
        print("{} : {}".format(i + 1, argv[i + 1]))
