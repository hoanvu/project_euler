# Find the largest prime factor of a number

# Every number n can at most have one prime factor greater than n . If we, after dividing out some prime factor, calculate the square root of the remaining number we can use that square root as upper limit for factor. If factor exceeds this square root we know the remaining number is prime.

import math

number = 600851475143

# Check for special case if the given number is divisible by 2
if number % 2 == 0:
    last_factor = 2
    number //= 2

    # If the number is still divisible by 2, keep dividing it by 2
    # The last_factor should be 2 anyway
    while number % 2 == 0:
        number //= 2
else:
    last_factor = 1

factor = 3
# Set the upper limit for factor
max_factor = math.sqrt(number)

while number > 1 and factor <= max_factor:
    if number % factor == 0:
        number //= factor
        last_factor = factor
        while number % factor == 0:
            number //= factor
        max_factor = math.sqrt(number)
    factor += 2

if number == 1:
    print (last_factor)
else:
    print (number)