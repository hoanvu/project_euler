# Calculate the largest palindrome number made by product of 2 3-digit numbers
# A palindrome number is a number that read the same both ways. Eg: 8118, 93239, ...
# =================================================================================== #

# Check whether a number is a palindrome by keep dividing it by 10
# and get the remainder
def isPalindrome(inputNumber):
	reverse = ""	# This string store the reversed of the input number

	# Store the input number to a temp variable
	# We need the inputNumber for last comparison
	temp = inputNumber 

	# As long as the number has more than 1 digits
	while temp > 10:
		# Find the last number by modulo, then convert to string, and add to 'reverse'
		reverse += str(temp % 10)
		temp /= 10	# then divide the number by 10 to remove the last number

	# Add the last number to the reverse
	reverse += str(temp)
	# Convert 'reverse' to integer
	reverse = int(reverse)

	# If reverse equals to input, then palindrome, 
	if reverse == inputNumber:
		return True
	# otherwise
	return False

# Keep multiplying 2 3-digit numbers until we find a largest palindrome
def main():
	# currPalindrome: store product of the current multiplication which is a palindrome
	# palindrome: 		store the largest palindrome we found so far
	# Do not use list for memory efficiency
	palindrome = -1
	currPalindrome = -1

	# Use 2 for loop, multiply all numbers between 100 and 999
	# Check for palindrome after each multiplication
	for number1 in range(100, 1000):
		for number2 in range(100, 1000):
			product = number1 * number2

			# If a product is a palindrome, check if it's the largest palindrome so far
			if isPalindrome(product):
				currPalindrome = product
				if currPalindrome > palindrome:
					palindrome = currPalindrome

	# Print only the largest palindrome
	print palindrome

if __name__ == "__main__":
	main()