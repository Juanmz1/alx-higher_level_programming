#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    add = 0
    for i in range(length):
        add += int(argv[i])
    print("{:d}2.format(add))
