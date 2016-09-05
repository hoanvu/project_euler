# https://projecteuler.net/problem=16

number = str(2 ** 1000)

result = 0
for digit in number:
    result += int(digit)

print result