#!/usr,bin/python3

if __name__ == '__main__':
    import sys

    num = len(sys.argv)
    if num == 0:
        print("{} argument.".format(num - 1))
    elif num == 1:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))
    for n in range(1, num):
        print("{}: {}".format(n, sys.argv[n]))
