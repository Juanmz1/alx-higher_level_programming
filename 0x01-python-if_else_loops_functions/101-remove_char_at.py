#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n < 0 or n > length:
        now = str
        return now
    now = ''
    for j in range(length):
        if j == n:
            continue
        now += str[j]
    return now
