
#   python program to move all the negative elements to one side of the array

def move_to_right(arr: list) : 
    left = 0;right = len(arr) - 1

    while left <= right : 
        if arr[left] < 0 : 
            arr[left], arr[right] = arr[right], arr[left]
            right-=1
        else : 
            left+=1


if __name__ == "__main__":
    arr = [1,2,-1,3,4,-5,6,-7,23,-56]
    move_to_right(arr)
    print(arr)