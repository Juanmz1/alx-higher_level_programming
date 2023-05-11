#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if c < 0 or c > length:
        now = str
        return now
    now = ''
    for j in range(length):
        if j == c:
            continue
        now += str[j]
    return now
