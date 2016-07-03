# https://projecteuler.net/problem=12
# What is the value of the first triangle number to have over five hundred divisors?

from __future__ import division


# This method returns a generator for all possible triangular numbers
def get_triangular_number(start):
    while True:
        yield ( start * (start + 1) ) // 2
        start += 1


# This method returns a set containing all factors for a given number
def get_factors(number):
    factors = set()
    factors.add(1)
    factors.add(number)

    half = number // 2
    for dividend in range(2, half + 1):
        if number % dividend == 0:
            factors.add(dividend)
            factors.add(number // dividend)

    return factors


if __name__ == '__main__':
    for tri in get_triangular_number(1):
        if len(get_factors(tri)) > 500:
            print (tri)
            break