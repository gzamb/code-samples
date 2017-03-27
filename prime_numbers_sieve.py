#!/usr/bin/python

################################
# Find Prime numbers using
# Sieve's algorithm.
# Gabriela Zambrano
# 3/25/17
################################
from math import sqrt
import sys


def main(args):
    number = int(args[0])
    print(is_prime(number))


def is_prime(number):
    is_prime_list = [True if x != 1 else False for x in range(1, number + 1)]

    for idx in range(3, len(is_prime_list)):
        if (idx + 1) % 2 == 0:
            is_prime_list[idx] = False

    square_root = int(sqrt(number))
    for p in range(3, square_root+1, 2):
        if is_prime_list[p-1]:
            for i in range(p*p, number + 1, 2*p):
                is_prime_list[i-1] = False

    prime_list = [idx + 1 for idx in range(len(is_prime_list))
                  if is_prime_list[idx]]

    return prime_list

if __name__ == "__main__":
    main(sys.argv[1:])
