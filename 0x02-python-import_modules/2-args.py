#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arguments = len(sys.argv)

    if(arguments-1 == 0):
        print("0 arguments.")
    else:
        print("{} arguments:".format(arguments-1))
        for i in range(1, arguments):
            print("{}: {}".format(i, argv[i]))
