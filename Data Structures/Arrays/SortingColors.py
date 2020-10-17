"""
75. Sort Colors
Medium

4110

240

Add to List

Share
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""

def sortArray(arr) : 

    left = 0;mid = 0
    right = len(arr) - 1

    while mid <= right : 
        el = arr[mid]        

        if el == 0 : 
            arr[left], arr[mid] = arr[mid], arr[left]
            left+=1
            mid+=1

        elif el == 1 : 
            mid+=1
            
        elif el == 2 : 
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1


if __name__ == '__main__' : 
    arr = [1,2,0,0,1,2,0,0,1,2,2,0,0]
    sortArray(arr)
    print(arr)
        