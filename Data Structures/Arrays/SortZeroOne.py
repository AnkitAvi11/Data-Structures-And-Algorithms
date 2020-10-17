"""
Sort an array of 0s, 1s and 2s 
Easy Accuracy: 48.12% Submissions: 100k+ Points: 2
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
"""

def sortOneTwo(arr : list) : 
    left = 0;mid=0;right=len(arr)-1

    while(mid <= right) : 
        if arr[mid] == 0 :
            arr[mid], arr[left] = arr[left], arr[mid] 
            left+=1;mid+=1
        elif arr[mid] == 1 :
            mid+=1
        else : 
            arr[mid], arr[right] = arr[right], arr[mid]
            right-=1


#   main function to run the code
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t) : 
        n = int(input())
        arr = list(map(int, input().split()))
        sortOneTwo(arr)
        for el in arr : 
            print(el, end = " ")
            
        print()