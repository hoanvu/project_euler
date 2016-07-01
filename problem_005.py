# Find the smallest number that evenly divisible by all of the numbers from 1 to 20

# For further divisibility rules, read the following link:
# https://en.wikipedia.org/wiki/Divisibility_rule
###################################################################################

import math

# Check whether a number is a prime number
def is_prime(number):
    if type(number) != int and type(number) != long:
        return False
    if number > 1:
        if number == 2: # 2 is a prime number
            return True
        if number % 2 == 0: # All prime number except 2 should be odd
            return False
        for currentNumber in range(3, int(math.sqrt(number) + 1), 2):
            if number % currentNumber == 0:
                return False

        return True
    return False

# Get the next prime number, using generator
def get_next_prime(start_number):
    while True:
        if is_prime(start_number):
            yield start_number
        start_number += 1

#
def get_factors():
    final = {}
    for number in range(2, 21):
        factors = []
        for prime in get_next_prime(2):
            if number % prime == 0:
                while number % prime == 0:
                    factors.append(prime)
                    number /= prime
            if number == 1:
                break

        factors = {factor: factors.count(factor) for factor in set(factors)}
        for factor, freq in factors.items():
            if not factor in final:
                final[factor] = 1
            else:
                if freq > final[factor]:
                    final[factor] = freq
    return final


if __name__ == '__main__':
    factors = get_factors()
    result = 1

    for factor, freq in factors.items():
        result *= math.pow(factor, freq)
    print (result)