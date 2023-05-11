#!/usr/bin/python3
for b in range(26):
    if b % 2 == 0:
        print('{:c}'.format(122 - b), end="")
    else:
        print('{:c}'.format(90 - b), end='')
