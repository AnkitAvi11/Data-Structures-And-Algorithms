
"""
    Program to solve the problem of two sum from leetcode
"""

def twoSum(arr : list, target : int) : 
    arr.sort()
    result = list()
    left = 0;right=len(arr) - 1

    while left < right : 
        current_sum = arr[left] + arr[right]
        if current_sum < target : 
            left+=1
        elif current_sum > target : 
            right-=1

        else : 
            result.extend([arr[left], arr[right]])
            break

    return result



if __name__ == '__main__' : 
    print(twoSum([-4,-1,1,3,5,6,8,11], 13))