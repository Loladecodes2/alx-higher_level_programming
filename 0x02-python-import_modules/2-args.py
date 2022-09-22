#!/usr,bin/python3

if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("No argument.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    for n in range(num):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
