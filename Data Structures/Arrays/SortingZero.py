

def sortingZero(arr: list) : 
    left = 0 ;mid = 0; right = len(arr) - 1

    while mid < right:
        if arr[mid] == 0 : 
            arr[left], arr[mid] = arr[mid], arr[left]
            left+=1;mid+=1
        elif arr[mid] == 1: 
            mid+=1
        else : 
            arr[mid], arr[right] = arr[right], arr[mid]
            right-=1
    else:
        pass


if __name__ == "__main__":
    arr = [1,0,2,1,1,0,0,1,2,2,0]
    sortingZero(arr)
    print(arr)
