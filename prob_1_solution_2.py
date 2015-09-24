# All numbers divisible by 3 would be: 3, 6, 9, 12, ... 
# Sum all of them together: 
# = (3 + 6 + 9 + 12 + ...)
# = 3 * (1 + 2 + 3 + 4 + ...)
# = 3 * ( (p * (p + 1)) / 2 )
#
# Similar for all numbers divisible by 5

lastValue = 999

def sumWhenDividedBy(n):
	p = lastValue / n
	return n * (p * (p + 1)) / 2

# We have to subtract the result from all number divisible by 15 
# because some numbers like 15, 30, 45, ... will be counted twice
print sumWhenDividedBy(3) + sumWhenDividedBy(5) - sumWhenDividedBy(15)