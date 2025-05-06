#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./factorial.py <integer>")

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1

    return result

f = factorial(int(sys.argv[1]))
print(f)
