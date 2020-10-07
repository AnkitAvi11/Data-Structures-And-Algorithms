
#   hackerrank problem of problem solving 
#   problem statement : Picking Numbers


def pickingNumbers(arr) : 
    left = 0
    max_sum = 0;max_left = 0;max_right=0

    for i in range(1, len(arr)) : 
        if abs(arr[i] - arr[i-1]) > 1 : 
            number = i - left
            if number > max_sum : 
                max_sum = number
                max_left = left
                max_right = i-1
            left = i
    
    return max_sum+1


if __name__ == "__main__" : 
    print(pickingNumbers([1, 2, 2, 3, 1, 2]))

