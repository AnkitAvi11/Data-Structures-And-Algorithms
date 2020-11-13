"""
Cyclically rotate an array by one
---------------------------------
Given an array, cyclically rotate an array by one
"""

def rotate_by_one(arr : list) : 

    i = len(arr) - 1
    temp = arr[i]
    while i>0 : 
        arr[i] = arr[i-1]
        i-=1

    arr[i] = temp


if __name__ == "__main__":
    arr = [9,8,7,6,4,2,1,3]
    rotate_by_one(arr)
    print(arr)

    