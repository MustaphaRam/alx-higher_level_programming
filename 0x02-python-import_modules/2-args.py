#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arguments = len(sys.argv)

    if arguments-1 == 0:
        print("0 arguments.")
    elif arguments-1 == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arguments-1))
        for i in range(1, arguments):
            print("{}: {}".format(i, argv[i]))
