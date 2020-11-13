
#   python program to find the union of two sorted arrays

def union_of_arrays(arr1: list, arr2: list) : 
    i=0;j=0
    result = set()
    while i<len(arr1) and j<len(arr1) : 
        if arr1[i] <= arr2[j] : 
            result.add(arr1[i])
            i+=1
        elif arr1[i] >= arr2[j] : 
            result.add(arr2[j])
            j+=1
    
    if i == len(arr1) :
        while j < len(arr2) : 
            result.add(arr2[j])
            j+=1
    else: 
        while i < len(arr1) : 
            result.add(arr1[i])
            i+=1

    return result



if __name__ == "__main__":
    print(union_of_arrays([1,2,3,4,5], [5,6,7,8]))
