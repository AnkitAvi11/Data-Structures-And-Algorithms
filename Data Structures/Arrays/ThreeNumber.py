#   Three number sum

def threeSumProblem(arr: list, target: int) : 
    arr.sort()
    result = list()
    
    for i in range(0, len(arr) - 2) : 
        left = i+1;right=len(arr)-1

        while left < right : 
            curren_sum = arr[i] + arr[left] + arr[right]

            if curren_sum == target : 
                result.append([arr[i], arr[left], arr[right]])
                left+=1
                right-=1
            elif curren_sum < target : 
                left+=1
            else : 
                right -= 1

    return result



if __name__ == '__main__' : 
    print(threeSumProblem([12,3,1,2,-6,5,-8,6], 0))