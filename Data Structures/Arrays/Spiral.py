
def spiralTraversal(arr) :
    result = list() 
    rowStart, rowEnd = 0, len(arr) - 1
    colStart, colEnd = 0, len(arr[0]) - 1

    while rowStart <= rowEnd and colStart <= colEnd : 

        for col in range(colStart, colEnd+1) : 
            result.append(arr[rowStart][col])

        for col in range(rowEnd, colEnd+1) : 
            result.append(arr[col][colEnd])

        for col in range(colEnd, rowStart) :
            result.append(arr[rowEnd][col])

        for col in range(rowEnd, rowStart+1) : 
            result.append(arr[col][colStart])

        rowStart += 1
        rowEnd -= 1
        colStart += 1
        colEnd -= 1

    return result


if __name__ == '__main__' : 
    spiralTraversal([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
