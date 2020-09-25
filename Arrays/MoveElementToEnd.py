#   Moving elements to the end

def moveToEnd(arr : list, sk : int) : 
    left = 0;right = len(arr)-1

    while left < right : 

        while arr[right] == sk : 
            right -= 1
        
        if arr[left] == sk : 
            arr[left], arr[right] = arr[right], arr[left]

        left += 1

    return arr

if __name__ == '__main__' : 
    print(moveToEnd([1,3,2,4,2,2,2], 2))