#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

print("Last digit of {} is {}".format(number, last_digit), end='')

if last_digit > 5:
    print(" It is greater than 5")
elif last_digit == 0:
    print(" It is 0")
else:
    print(" It is less than 6 and not 0")
