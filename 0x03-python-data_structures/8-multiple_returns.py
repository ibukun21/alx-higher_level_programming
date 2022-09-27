#!/usr/bin/python3

def multiple_returns(sentence):
    Slen = len(sentence)
    if Slen > 0:
        return (Slen, sentence[0])
    return (0, None)
