# Calculate the largest palindrome number made by product of 2 3-digit numbers
# A palindrome number is a number that read the same both ways. Eg: 8118, 93239, ...
# =================================================================================== #

# The product of 2 3-digit numbers is a 6-digit number, and can be expressed as a palindrome: xyzzyx:
# xyzzyx = 100000x + 10000y + 1000z + 100z + 10y + x
#        = 100001x + 10010y + 1100z
#        = 11 * ( 9091x + 910y + 100z )
# From above equation, at least one of the numbers must be divisible by 11
# We can use this clue to decide the next step for the second number


def is_palindrome(number):
    return str(number) == str(number)[::-1]


result = -1
first = 999
while first >= 100:
    # if first number is divisble by 11, set the second number to 999 and steps to 1
    # otherwise, set second number to 990, which is the largest number divisible by 11
    # and keep decreasing by 11
    if first % 11 == 0:
        second = 999
        steps = 1
    else:
        second = 990
        steps = 11

    # Always begin the inner loop by setting the second number equal to the first
    while second >= first:
        product = first * second

        # If the product of 2 number already less than the stored palindrome, skip to the next number
        if product <= result:
            break

        # otherwise, check for palindrome and assign new number to result
        if is_palindrome(product):
            result = first * second

        second -= steps
    first -= 1

print (result)