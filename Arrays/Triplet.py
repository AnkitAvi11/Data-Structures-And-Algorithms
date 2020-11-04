#   Three number sum program
#   We will be using the sliding window algorithm here as well which will give us the complexity of O(nlogn)

def sum_of_three(arr) : 
    result = 0
    arr.sort()
    
    for i in range(len(arr)-2) : 
        left = i+1;right=len(arr)-1
 
        while left < right : 
            x=arr[i];y=arr[left];z=arr[right]
            if y-x == z-y : 
                result+=1
                left+=1
                right-=1
            elif y-x < z-y : 
                left += 1
            elif y-x > z-y :
                right -= 1
    else : 
        print("Done with the loop")
    return result+1

if __name__ == '__main__' :     
    print(sum_of_three([2,5,6,8,10]))
