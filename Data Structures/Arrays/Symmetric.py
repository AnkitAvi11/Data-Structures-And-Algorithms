#   program to check if the given matrix is symmetric 
#   a matrix is said to be symmetric if A = A`

import math

def isSymmetric(arr) -> bool :

    for i in range(len(arr)) : 
        for j in range(len(arr[i])) : 
            if arr[i][j] != arr[len(arr[i])-i-1][j] : 
                return False
    return True


if __name__ == '__main__' : 
    print(isSymmetric([[8],[8],[8]]))


"""
 [ 00, 01, 02, 03 ]
 [ 10, 11, 12, 13 ]
 [ 20, 21, 22, 23 ]
 [ 30, 31, 32, 33 ]

"""