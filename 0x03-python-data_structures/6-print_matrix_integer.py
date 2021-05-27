#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(0, len(i), 1):
            if (x < (len(i)-1)):
                print("{}".format(i[x]), end=" ")
            else:
                print("{}".format(i[x]), end='')
        print()
