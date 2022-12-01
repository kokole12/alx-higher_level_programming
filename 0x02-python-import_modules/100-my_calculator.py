#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mull
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.arg[2] not in list(ops.kys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = sys.arg[1]
    b = sys.arg[3]
    print("{} {} {} = {}".format(a, sys.arg[2], b, ops[sys.arg[2]](a, b)))
