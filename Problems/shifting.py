"""
arr = [1,10,3,4,5,2,2,5,6,7,8,9,2,2]
target_element = 2
output = find all the occurences of target_element and move it on the right/left side of the list or array

"""

#   swapping method
def shift_using_swapping(arr : list, target : int) : 
    left = 0;right = len(arr) - 1

    while left <= right : 
        
        while arr[right] == target : right-=1

        if arr[left] == target : 
            #   swapping
            arr[left], arr[right] = arr[right], arr[left]
            right-=1

        left += 1 


def shiting_using_iteration(arr : list, target : int) : 

    for i in range(1, len(arr)) :
        temp = arr[i]
        j = i - 1
        while j>=0 and temp == target : 
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = temp



if __name__ == "__main__":
    arr = [1,10,3,4,5,2,2,5,6,7,8,9,2,2]

    shiting_using_iteration(arr, 2)

    print(arr)



