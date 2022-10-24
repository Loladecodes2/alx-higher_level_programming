#!/usr/bin/python3
"""
A class MyList that inherits from list:
"""


class MyList(list):
    '''MyList inherit list'''
    def print_sorted(self):
        '''prints the sorted list'''
        print(sorted(self))
