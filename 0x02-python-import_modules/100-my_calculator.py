#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length_1 = len(argv) - 1
    ope = "+-*/"
    if length_1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ope:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    for i in ope:
        if argv[2] == i:
            sign = i
    a = int(argv[1])
    b = int(argv[3])
    if sign == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif sign == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif sign == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif sign == '/':
        print(f"{a} / {b} = {div(a, b)}")
