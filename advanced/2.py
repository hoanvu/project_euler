# Sum all even Fibonacci numbers
MAX = 4000000

first = 1
second = 1
third = first + second
sumFib = 0

# We don't need to check for even Fibonacci because every third Fibonacci number is always even
while second < MAX:
	sumFib += third
	first = second + third
	second = first + third
	third = first + second

print sumFib