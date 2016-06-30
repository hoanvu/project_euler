# Calculate the largest palindrome number made by product of 2 3-digit numbers
# A palindrome number is a number that read the same both ways. Eg: 8118, 93239, ...
# =================================================================================== #


def is_palindrome(number):
    """
    Check whether a number is a palindrome or not
    :param number: input number to be checked
    :return: True if input number is a palindrome, False otherwise
    """
    return str(number) == str(number)[::-1]

# Keep multiplying 2 3-digit numbers until we find a largest palindrome
def main():
    # currPalindrome: store product of the current multiplication which is a palindrome
    # palindrome: 		store the largest palindrome we found so far
    # Do not use list for memory efficiency
    result = -1

    # Use 2 for loop, multiply all numbers between 999 and 100 inclusively
    # At the start of each second for loop, we assign `second` to the value of `first`
    # This will reduce roughly half the amount of operations needed
    for first in range(999, 99, -1):
        for second in range(first, 99, -1):
            product = first * second
            if is_palindrome(product) and result < product:
                result = product

    # Print only the largest palindrome
    print (result)

if __name__ == "__main__":
    main()