#   Monotonic array optimised solution
#   Time complexity = O(n)  |   Space Complexity : O(1)


#   method to check if the direction breaks
def directionChanged(direction, previous, current) : 
    difference = current - previous
    print(direction, difference)
    if direction > 0 : 
        return difference < 0
    
    return difference > 0


#   function to check if the array is monotic or not
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


#   driver code
if __name__ == '__main__' : 
    print(isMonotonicArray([1,2,3,4,5]))