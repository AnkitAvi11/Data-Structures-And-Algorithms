#   leetcode amrstrong problem
import math

def is_armstrong(num : int) : 
    k = math.floor(math.log10(num)) + 1
    
    summation, temp = 0, num

    while temp != 0 : 
        r = temp % 10 
        summation += r**k
        temp //= 10 

    print(k, summation, num)

    if summation == num : 
        return True

    return False


if __name__ == '__main__' : 
    print(is_armstrong(253))


