#   program to check if the given number is palindrome or not

def ispalindrome(num : int) -> bool : 
    new_num = 0;temp = num

    while temp != 0 : 
        new_num = new_num*10 + temp%10 
        temp //= 10

    return new_num == num


if __name__ == '__main__' : 
    print(ispalindrome(1111))
