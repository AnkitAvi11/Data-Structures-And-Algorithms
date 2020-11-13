
#   python program to check whether a given array is monotonic of not

def changeDirection(direction, previous_num, current_num):
    difference = current_num - previous_num
    if direction > 0 : 
        return difference < 0
    return difference > 0

#   actual function thats going to check
def is_monotic(arr) : 
    
    if len(arr) <= 2 : 
        return True


    direction = arr[1] - arr[0]

    for i in range(2, len(arr)) : 
        if direction == 0 : 
            direction = arr[i] - arr[i-1]
            continue
        
        if changeDirection(direction, arr[i-1], arr[i]) : 
            return True
        
    return False
        


if __name__ == '__main__' : 
    print(is_monotic([-1,-5,-10,-1100,-1100, -1101, -1102, -9001, 0, 23]))
    print(is_monotic([1,2,3,4,5]))