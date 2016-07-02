# The following iterative sequence is defined for the set of positive integers:

# n -> n/2    (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?


# This method returns the Collatz sequence from the given number
def get_sequence(number):
    sequence = [number]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return sequence


if __name__ == '__main__':
    longest = 0
    result = 0
    for number in range(1, 1000000):
        seq_length = len(get_sequence(number))
        if longest < len(get_sequence(number)):
            longest = seq_length
            result = number

    print ("Number {} produces the longest chain with length: {}".format(result, longest) )