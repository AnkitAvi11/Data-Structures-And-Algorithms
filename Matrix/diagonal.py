
"""
Diagonal matrix program
"""

#   method to check if the given matrix is a diagonal matrix or not
def is_diagonal_matrix(arr) : 

    for i in range(len(arr)) : 
        for j in range(len(arr[i])) : 
            if i == j : 
                if arr[i][j] == 0 : 
                    return False

            else : 
                if arr[i][j] != 0 : 
                    return False
    else : 
        print("Loop ends here ... ")


    return True


def is_lower_triangle_matrix(arr) : 

    for i in range(len(arr)) : 
        for j in range(len(arr[i])) : 
            if j > i : 
                if arr[i][j] != 0 : 
                    return False

            else : 
                if arr[i][j] == 0 : 
                    return False


    return True



#   driver code of the program
if __name__ == '__main__' : 

    arr = [
        [2,0,0,0,0],
        [1,7,0,0,0],
        [2,3,4,0,0],
        [1,1,1,9,0],
        [1,2,2,2,6]
    ]

    print(is_diagonal_matrix(arr))
    print(is_lower_triangle_matrix(arr))
