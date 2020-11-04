"""
QUESTION STATEMENT : MERGE TWO SORTED ARRAYS WITHOUT USING ANY EXTRA SPACE

example :

arr1 = {1,3,5,7,9} size = n
arr2 = {2,4,6,8,10} size = m

arr1 after merging = {1,2,3,4,5,6,7,8,9,10}

"""

def mergeArrays(arr : list, arr2 : list) : 

    i = 0;j = 0;

    while i < len(arr) : #  O(n)
        if arr[i] > arr2[j] : 
            arr[i], arr2[j] = arr2[j], arr[i]   #   swapping the elements

            arr2.sort()     #   O(mlog2m)

        i+=1

    #   total complexity = (n*m)log2m

    for el in arr2 : 
        arr.append(el)


if __name__ == '__main__' : 
    arr = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]

    mergeArrays(arr, arr2)

    print(arr)

    
