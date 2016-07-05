# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first
# 100 natural numbers and the square of the sum

# Limit
N = 100000

sum = (N * ( N + 1 )) / 2
square_of_sum = sum * sum

sum_of_squares = ( N * ( N + 1 ) * ( 2 * N + 1 ) ) / 6

print square_of_sum - sum_of_squares