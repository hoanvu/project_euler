# Calculate the largest palindrome number made by product of 2 3-digit numbers
# A palindrome number is a number that read the same both ways. Eg: 8118, 93239, ...
# =================================================================================== #

# Check whether a number is a palindrome by keep dividing it by 10
# and get the remainder
def is_palindrome(number):
	return True if str(number) == str(number)[::-1] else False

# Keep multiplying 2 3-digit numbers until we find a largest palindrome
def main():
	# currPalindrome: store product of the current multiplication which is a palindrome
	# palindrome: 		store the largest palindrome we found so far
	# Do not use list for memory efficiency
	palindrome = -1

	# Use 2 for loop, multiply all numbers between 100 and 999
	# Check for palindrome after each multiplication
	for number1 in range(100, 1000):
		for number2 in range(100, 1000):
			product = number1 * number2

			# If a product is a palindrome, check if it's the largest palindrome so far
			if is_palindrome(product):
				curr_palindrome = product
				if curr_palindrome > palindrome:
					palindrome = curr_palindrome

	# Print only the largest palindrome
	print (palindrome)

if __name__ == "__main__":
	main()