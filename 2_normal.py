# Sum all even Fibonacci numbers
MAX = 4000000

first = 1
second = 1
sumFib = 0

# Function to check whether a number is even
def isEven(number):
	return number % 2 == 0

while second < MAX:
	next = first + second
	first = second
	second = next
	if isEven(second):
		sumFib += second

print sumFib