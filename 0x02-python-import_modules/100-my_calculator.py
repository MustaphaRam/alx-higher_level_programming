#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    arguments = len(sys.argv)
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if arguments-1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] in list(op.keys()):
            print("{} {} {} = {}".format(a, argv[2], b, op[argv[2]](a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
