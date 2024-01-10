#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for i in sorted(my_dict.keys()):
        print("{}: {}".format(i, my_dict[i]))
