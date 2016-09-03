# https://projecteuler.net/problem=25

# Initialize first 3 Fibonacci numbers
f1 = 1
f2 = 1
f3 = f1 + f2

# Keep track of the index
index = 3

# Continue until we get the Fibonacci number with 1000 digits
while len(str(f3)) < 1000:
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    index += 1

# Print the result
print f3
print 
print index