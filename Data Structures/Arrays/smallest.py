
#   python program to find the smallest difference among two ararys

def smallest_difference(arr1 : list, arr2: list) : 
    arr1.sort()
    arr2.sort()

    i = 0;j = 0;
    smallest_diff = float("inf")
    result = [arr1[0], arr2[0]]
    while i < len(arr1) and j < len(arr2) : 
        difference = arr1[i] - arr2[j]
        if arr1[i] < arr2[j] : 
            i+=1
        elif arr1[i] > arr2[j] : 
            j+=1
        else : 
            return [arr1[i], arr2[j]]
        
        if difference < smallest_diff : 
            result = [arr1[i-1], arr2[j-1]]

    return result


if __name__ == '__main__' : 
    print(smallest_difference([-1,5,10,20,28,3], [26,134,135,15,17]))