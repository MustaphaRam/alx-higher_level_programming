#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new_list = my_list[:]
        new_list[idx] = element
    else:
        return my_list
    return (new_list)
