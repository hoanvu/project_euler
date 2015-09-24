# Find the smallest number that evenly divisible by all of the numbers from 1 to 20

# For further divisibility rules, read the following link:
# https://en.wikipedia.org/wiki/Divisibility_rule
###################################################################################

import math

# This variable store the biggest number to be divisible by. For eg: if you need to 
# find a number that divisible by all number from 1 to 15, this UPPER_END must be set to 15
UPPER_END = 20

def isPrime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for currentNum in range(int(math.sqrt(number) + 1), 2):
			if number % currentNum == 0:
				return False
		return True
	return False

def generatePrimes():
	p = []
	for number in range(1, UPPER_END + 1):
		if isPrime(number):
			p.append(number)

	return p

def main():
	# This variable store the smallest multiple
	result = 1

	index = 0
	check = True
	expLimit = math.sqrt(UPPER_END)

	p = generatePrimes();
	a = []

	for i in range(index, len(p) + 1):
		a.append(i)
	print len(a)

	while p[index] <= UPPER_END:
		a[index] = 1
		if check:
			if p[index] <= expLimit:
				a[index] = math.floor( math.log(UPPER_END) / math.log(p[index]) )
			else:
				check = False

		result *= math.pow( p[index], a[index] )
		print index
		index += 1

	print result

if __name__ == "__main__":
	main()