#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest = 0
    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
    for key, value in a_dictionary.items():
        if value == largest:
            return key
