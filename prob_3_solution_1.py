# Calculate the largest prime factor of a number

import math

# Check whether a number is a prime number
def isPrime(number):
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
def getNextPrime(startNumber):
	while True:
		if isPrime(startNumber):
			yield startNumber
		startNumber += 1

# Keep dividing the input number with primes yielded from getNextPrime()
# If divisible, push it to a list
# Return the last element
def main():
	number = 600851475143	# input number
	result = -1 	# This stores the biggest prime factor

	# Keep getting the next prime number, starting from 2
	for prime in getNextPrime(2):
		# As long as the number is greater than 1
		if number > 1:
			# And it's divisible by a prime number
			if number % prime == 0:
				result = prime 	# Assume that prime number to be the result
				number /= prime 
		else:
			# Print result when number is 1, which means there is no more prime number to divide
			print result
			return

if __name__ == "__main__":
	main()