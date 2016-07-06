# https://projecteuler.net/problem=1
# Find sum of all multiples of 3 and 5
#
# All numbers divisible by 3 would be: 3, 6, 9, 12, ...
# Sum all of them together:
# = (3 + 6 + 9 + 12 + ...)
# = 3 * (1 + 2 + 3 + 4 + ...)
#
# Similar for all numbers divisible by 5
from __future__ import division

MAX_VALUE = 999

def sum_divisible_by(n):
    p = MAX_VALUE // n
    return ( n * p * (p + 1) ) // 2


# We have to subtract the result from all number divisible by 15
# because some numbers like 15, 30, 45, ... will be counted twice
if __name__ == '__main__':
    print( sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15) )