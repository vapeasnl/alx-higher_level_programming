#!/usr/bin/python3
def no_c(my_string):
    nstr = my_string.translate({ord(i): None for i in 'cC'})
    return nstr
