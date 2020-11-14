
#   merge without extra space

def merge_two(arr1 : list, arr2 : list) : 

    i = 0;j = 0

    while i < len(arr1) and j < len(arr2) : 
        if arr1[i] >= arr2[j] : 
            arr1[i], arr2[j] = arr2[j], arr1[i]
            arr2.sort()
        
        i+=1


    for el in arr2 : 
        arr1.append(el)


if __name__ == '__main__' : 
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]

    merge_two(arr1, arr2)

    print(arr1)


