#   program to find the number of digits in a given number
import math

def calDigits(num : int) : 
    return math.log10(num)

if __name__ == '__main__' : 
    print(math.ceil(calDigits(12345)))