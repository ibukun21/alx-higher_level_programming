#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for j in range(list_length):
        try:
            div = 0
            div = my_list_1[j] / my_list_2[j]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            newList.append(div)
    return newList
