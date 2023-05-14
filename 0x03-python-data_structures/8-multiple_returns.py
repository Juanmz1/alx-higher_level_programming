#!/usr/bin/python3
def multiple_returns(sentence):
    charater_1 = sentence[0]
    length_sen = len(sentence)
    if length_sen < 0:
        character_1 = None
        return (length_sen, None)
    else:
        return (length_sen, character_1)
