#!/usr/bin/python3

def multiple_returns(sentence):
    mytpl = ()
    if len(sentence) == 0:
        mytpl = 0, "None"
    else:
        mytpl = len(sentence), sentence[0]

    return mytpl
