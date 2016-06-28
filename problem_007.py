# Calculate the 10,001st prime number
# For example: 13 is the 6th prime number (2, 3, 5, 7, 11, 13, 17, ...)

import math

# Function to check whether a number is a prime number
def isPrime(number):
	if number > 1:		# Prime number must bigger than 1 and not a negative number
		if number == 2:		# 2 is a prime number
			return True
		if number % 2 == 0:
			return False
		for currentNumber in range(3, int(math.sqrt(number) + 1), 2):
			if number % currentNumber == 0:
				return False

		return True
	return False

# Using generator to get the next prime number
# This is a better way because we don't know when to stop
def getNextPrime(startNumber):
	while True:
		if isPrime(startNumber):
			yield startNumber
		startNumber += 1

# Get the 10001st prime number
# Simply check each number whether it is a prime.
# If yes, increase the count until reach 10001
def main():
	count = 1		# we already have 2 is the first prime number
	for number in getNextPrime(3):
		if count < 10001 - 1:
			count += 1
		else:
			print number
			return

if __name__ == "__main__":
	main()