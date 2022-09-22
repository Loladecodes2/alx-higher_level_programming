#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1
    if num == 1:
        print("1 argument:")
    elif num == 0:
        print("0 argument.")
    else:
        print("{} argument:".format(num))
    for n in range(num):
        print("{} : {}".format(n + 1, sys.argv[n + 1]))
