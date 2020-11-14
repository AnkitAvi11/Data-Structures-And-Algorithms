"""

Minimum number of jumps
-----------------------
Given an array of integers where each element represents the max number of steps that can be made forward from that element.
Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). if an 
element is 0, then cannot move through that element.

"""

def jump(arr : list) : 
    
    i = 0;step_count = 0

    if len(arr) <= 1 : 
        return 0

    while i < len(arr) : 
        
        if i >= len(arr) - 1 : 
            return step_count
        else : 
            if arr[i] != 0 : 
                step_count += 1

        if arr[i] == 0 : 
            i += 1
        else : 
            i += arr[i]

    return step_count


if __name__ == '__main__' : 
    print(jump([1,3,5,8,9,2,6,7,6,8,9]))


