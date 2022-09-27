#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for arr in matrix:
            for n in arr:
                if n != arr[-1]:
                    print("{:d}".format(n), end=" ")
                else:
                    print("{:d}".format(n))


