#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # check if the index is greater than or equal to the length of list
    if idx < 0 or idx >= len(my_list):
        return my_list
    # replace the element at that index in my_list.
    my_list[idx] = element
    return my_list
