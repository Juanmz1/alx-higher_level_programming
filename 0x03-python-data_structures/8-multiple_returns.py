#!/usr/bin/python3
def multiple_returns(sentence):
    charater_1 = sentence[0]
    length_sen = len(sentence)
    if length_sen == 0:
        return (charater_1, None)
    return (length_sen, charater_1)
