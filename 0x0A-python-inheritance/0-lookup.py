#!/usr/bin/python3
""" function that define available attributes and methods of an object. """


def lookup(obj):
    '''
    function: lookup()
    returns: a list object
    '''
    return (dir(obj))
