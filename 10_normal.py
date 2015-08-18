# Calculate sum of all prime numbers smaller than 2,000,000

import math

# Get all primes number under 2 millions
LIMIT = 2000000

# Function to check whether a number is a prime number
def isPrime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for currentNumber in range(3, int(math.sqrt(number) + 1), 2):
			if number % currentNumber == 0:
				return False

		return True
	return False

# A generator to keep counting and checking for whether a number is a prime number
def getPrimes(startNumber):
	while True:
		if isPrime(startNumber):
			yield startNumber
			#print startNumber

		startNumber += 1

# Use the getPrimes() generator to count sum of all prime numbers
def sumPrimes():
	total = 2
	
	for number in getPrimes(3):
		if number < LIMIT:
			total += number
		else:
			print total
			return

def main():
	sumPrimes()

if __name__ == "__main__":
	main()