#   Monotonic array optimised solution

def directionChanged(direction, previous, current) : 
    difference = current - previous
    print(direction, difference)
    if direction > 0 : 
        return difference < 0
    
    return difference > 0

def isMonotonicArray(arr : list) -> bool : 
    
    if len(arr) <= 2 : 
        return True

    direction = arr[1] - arr[0]
    
    for i in range(2, len(arr)) : 
        if direction == 0 : 
            direction = arr[i] - arr[i-1]
            continue

        if directionChanged(direction, arr[i-1], arr[i]) : 
            return True
            
    return False


if __name__ == '__main__' : 
    print(isMonotonicArray([1,2,3,4,5]))