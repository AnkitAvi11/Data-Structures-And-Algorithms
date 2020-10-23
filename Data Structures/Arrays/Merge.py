#   program to merge to arrays a and b which are in ascending order and the result should be in descending order


def merge(arr : list, arr2 : list) : 
    i, j = 0, 0
    result = list()

    while i < len(arr) and j < len(arr2) : 
        if arr[i] <= arr2[j] : 
            result.append(arr[i])
            i += 1

        elif arr[i] >= arr2[j] : 
            result.append(arr2[j])
            j += 1

        
    if i == len(arr) : 
        result.append(arr2[j])
        j += 1
    else : 
        result.append(arr[i])
        i += 1

    return result


if __name__ == '__main__' : 
    print(merge([1,3,5,7,9],[2,4,6,8]))