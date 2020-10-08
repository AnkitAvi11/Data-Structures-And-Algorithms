#   Problem statement : Moving all the instances of a given element to the end of the array

def moveToEnd(arr : list, num : int) :

    left = 0;right = len(arr) - 1

    while(left < right) : 
        while arr[right] == num : 
            right -= 1

        if arr[left] == num : 
            arr[left], arr[right] = arr[right], arr[left]

        left+=1        

    return arr


if __name__ == '__main__' : 
    print(moveToEnd([1,2,2,2,3,4,5,2,2,4], 2))