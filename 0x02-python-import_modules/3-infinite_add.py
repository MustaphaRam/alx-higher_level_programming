#!/usr/bin/python3
import sys

argv = sys.argv
arguments = len(sys.argv)

if(arguments-1 == 0):
    print("0")
else:
    res = 0
    for i in range(1, arguments):
        res += int(argv[i])
    print("{}".format(res))
