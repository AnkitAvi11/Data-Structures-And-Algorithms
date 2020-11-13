#   python program to move a given element to the end of the array

def move_to_end(arr : list, target : int) : 
    left = 0;right=len(arr)-1

    while left < right : 

        while arr[right] == target : right-=1

        if arr[left] == target : 
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1

        left+=1


if __name__ == '__main__' : 
    arr = [2,1,2,2,2,3,4,2]

    move_to_end(arr, 2)

    print(arr)
