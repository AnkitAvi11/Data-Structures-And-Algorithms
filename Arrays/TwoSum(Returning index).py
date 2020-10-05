#   Leetcode 2 sum problem
#   returning the index of the array

def twoSum(nums : list, target : int) -> list : 

    for i in range(len(nums) - 1) : 
        for j in range(i+1, len(nums)) : 
            current_sum = nums[i] + nums[j]
            if current_sum == target : 
                return [i, j]

    return [-1, -1]

if __name__ == '__main__' : 
    print(twoSum([2,7,11,15], 9))