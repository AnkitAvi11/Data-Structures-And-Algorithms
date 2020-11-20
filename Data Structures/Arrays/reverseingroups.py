"""
Python program to reverse array in groups

"""
import math

#   function to reverse the array in groups
def reverse_in_groups(arr : list, start : int, end : int) : 

    while start < end : 
        arr[start], arr[end] = arr[end], arr[start]
        start+=1;end-=1



#   main driver of the program for this problem statement
if __name__ == '__main__' : 
    k = int(input("Enter the value of number of groups : "))

    arr = [1,2,3,4,5,6,7]

    start = 0 
    end = k-1

    if len(arr) % k == 0 : 
        print("inside here")
        for _ in range(len(arr) // k) : 
            reverse_in_groups(arr, start, end)
            start = start+k
            end = end+k
    
    else : 
        print("entered here")
        for _ in range(len(arr) // k) : 
            reverse_in_groups(arr, start, end)
            start = start+k
            end = end+k
        
        reverse_in_groups(arr, start, len(arr)-1)

    print(arr)



