
#   python program to find the intersection between two arrays

def intersection_arrays(arr1 : list, arr2: list) : 
    i=0;j=0;

    result = set()

    while i<len(arr1) and j<len(arr2) : 
        if arr1[i] < arr2[j] : 
            i+=1

        elif arr1[i] > arr2[j] : 
            j+=1

        else : 
            result.add(arr1[i])
            i+=1;j+=1

    return result


if __name__ == "__main__":
    print(intersection_arrays([1,2,3,4,5], [4,5,6,7,8,9]))
