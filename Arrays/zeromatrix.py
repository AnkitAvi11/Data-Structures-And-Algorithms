"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
"""

def printMatrix(arr) : 
    for rows in arr : 
        for el in rows : 
            print(el, end = " : ")

        print()

    return

def zeroMatrix(arr) : 
    i = 0
    while i < len(arr) : 
        j = 0
        try : 
            while j < len(arr[i]) : 
                if arr[i][j] == 0 : 
                    for k in range(len(arr[i])) : 
                        arr[i][k] = 0

                    for k in range(len(arr)) : 
                        arr[k][i] = 0

                    i+=1
                    j = i+1

                j+=1
        except :
            pass

        i+=1

if __name__ == '__main__' : 
    arr = [
        [1,0,3],
        [4,5,6],
        [7,8,9]
    ]
    #zeroMatrix(arr)
    printMatrix(arr)