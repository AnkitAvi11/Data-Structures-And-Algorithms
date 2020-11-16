#   leetcode amrstrong problem
import math


#   method to check if the given number is armstrong or not
def is_armstrong(num : int) : 
    k = math.floor(math.log10(num)) + 1
    
    summation, temp = 0, num

    while temp != 0 : 
        r = temp % 10 
        summation += math.floor(math.pow(r, k))
        temp //= 10 

    #   for debugging (remove if you want to)
    print(k, summation, num)

    #   checking if the sum is equal to the number given
    if summation == num : 
        return True

    #   returns false if the number is not armstrong
    return False


if __name__ == '__main__' : 
    print(is_armstrong(153))


