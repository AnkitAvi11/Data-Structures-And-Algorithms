"""
Hackerrank Hourglass Solution
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    largest = -float("inf");pos=-1
    for i in range(1, len(arr) -1) : 
        for j in range(1, len(arr[i])-1) : 
            sum = arr[i][j] + arr[i-1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j]+arr[i+1][j-1]+arr[i+1][j+1]
            if sum > largest : 
                largest = sum
                pos = (i, j)
    
    return(largest)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
