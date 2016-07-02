# The following iterative sequence is defined for the set of positive integers:

# n -> n/2    (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?


result = 0
longest = 1
for number in range(500001, 1000000, 2):
    count = 1
    temp = number
    while temp != 16:
        if temp % 2 == 0:
            temp >>= 1
        else:
            temp = 3 * temp + 1
        count += 1

    if longest < count:
        longest = count
        result = number

print result