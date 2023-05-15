#!/usr/bin/python3
def multiple_returns(sentence):
    charater_1 = sentence[0]
    length_sen = len(sentence)
    if length_sen > 0:
        return (length_sen, charater_1)
    return (length_sen, None)
