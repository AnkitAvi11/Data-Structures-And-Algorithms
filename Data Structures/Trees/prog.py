
#   method to calculate the factorial of a number
def factorial(num : int) -> int : 
    fact = 1
    for i in range(2, num+1) : 
        fact*=i
    
    return fact


if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    for el in mylist : 
        print("Factorial of {} = {}".format(el, factorial(el)), end="\r\n")
    
    for el, index in enumerate(mylist) : 
        print(el, index)