#!/usr/bin/python3

def no_c(my_string):
    # initialize an empty string new_string that will hold the modified version
    new_string = ""
    for char in my_string:
        if char.lower() not in ['c', 'C']:
            new_string += char
    # return the modified string
    return new_string
