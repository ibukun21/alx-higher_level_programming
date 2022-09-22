#!/usr/bin/python3
for a in range(97, 123):
    if (a is not 101) and (a is not 113):
        print("{:c}".format(a), end="")
