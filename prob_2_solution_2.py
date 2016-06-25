# Find sum of all even Fibonacci numbers
# First few Fibonacci numbers:
#               1  1  2  3  5  8  13  21  34  55  89  144
# Position:     1  2  3  4  5  6  7   8   9   10  11  12
# => every 3rd Fibonacci is even (at position 3, 6, 9, 12, ...)
# We only need to keep track of this third number

MAX_VALUE = 4000000

first = 1
second = 1
third = first + second
sum_even_fibo = 0

# Continue until the term does not exceed 4 millions
while second <= MAX_VALUE:
    # Update the sum
    sum_even_fibo += third

    # Update next 3 Fibonacci number
    first = second + third
    second = third + first
    third = first + second

print (sum_even_fibo)