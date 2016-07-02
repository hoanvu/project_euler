# 1 = 'one' => 3 letters
# 11 = 'eleven' => 6 letters
# 123 = 'one hundred and twenty three' => 24 letters without spaces or special characters
# => count all letters used by all numbers from 1 to 1000 inclusively

# This method returns a dictionary that contains all mapping from number to character representation
# for basic numbers that can be used to form all other numbers
def get_corpus():
    number_to_word = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        1000: 'one thousand'
    }
    teen = [14, 16, 17, 18, 19]
    ty = [60, 70, 80, 90]

    for number in teen:
        # 18 = 'eighteen' has only 1 't'
        ext = 'teen' if number != 18 else 'een'
        number_to_word[number] = number_to_word[number % 10] + ext

    for number in ty:
        # 80 = 'eighty' has only 1 't'
        ext = 'y' if number == 80 else 'ty'

        number_to_word[number] = number_to_word[number / 10] + ext

    for number in range(100, 901, 100):
        number_to_word[number] = number_to_word[number / 100] + ' hundred'

    return number_to_word


# Translate a given number to its character representation
def translate(number):
    number_to_word = get_corpus()

    # if the input number is already in the corpus, simply return its character representation
    if number in number_to_word:
        return number_to_word[number]
    # otherwise
    else:
        # if input number is between 21 and 99 (2 numbers)
        if 20 < number < 100:
            first = number - (number % 10)
            return number_to_word[first] + ' ' + number_to_word[number % 10]
        # if input number is between 100 and 999 (3 numbers)
        elif 100 <= number < 1000:
            first = number - (number % 100)
            return number_to_word[first] + ' and ' + translate(number % 100)


if __name__ == '__main__':
    length = 0
    for number in range(1, 1001):
        length += len(translate(number).replace(' ', ''))

    print (length)