#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement n to avoid infinite loop
    return result

# Ensure there's an argument and it's a valid integer
if len(sys.argv) != 2:
    print("Usage: {} <non-negative integer>".format(sys.argv[0]))
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError
except ValueError:
    print("Please provide a non-negative integer.")
    sys.exit(1)

f = factorial(num)
print(f)
