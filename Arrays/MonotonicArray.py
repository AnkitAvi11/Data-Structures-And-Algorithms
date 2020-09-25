#   Problem Statement : Check whether the given array is a Monotonic array

def isIncreasing(arr : list) -> bool : 
    for i in range(len(arr) - 1) : 
        if arr[i] > arr[i+1] :
            return False

    return True

def isDecreasing(arr) : 
    for i in range(len(arr) - 1) : 
        if arr[i] < arr[i+1] : 
            return False
    return True

def isMonotic(arr : list) -> bool : 
    if isIncreasing(arr) or isDecreasing(arr) : 
        return False
    else : 
        return True


if __name__ == '__main__' : 
    print(isMonotic([-1,-5,-10,-1100, -1101, -900]))