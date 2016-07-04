# Find the sum of the digits in the number 100!

def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)


if __name__ == '__main__':
    result = 0
    for n in str(fact(100)):
        result += int(n)

    print (result)