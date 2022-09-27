#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    Ta = resolve(tuple_a)
    Tb = resolve(tuple_b)
    return (Ta[0] + Tb[0], Ta[1] + Tb[1])


def resolve(T=()):
    Tlen = len(T)
    if Tlen == 0:
        Tnew = 0, 0
    elif Tlen == 1:
        Tnew = T[0], 0
    else:
        Tnew = T[0], T[1]
    return Tnew
