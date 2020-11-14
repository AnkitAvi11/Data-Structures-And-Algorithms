#   given an array with n integers and an integer k, find the numbers of pairs of elements in the array whose sum is equal to k

def find_pairs(arr : list, target : int) : 
    arr.sort()
    left = 0;right = len(arr) - 1
    result = list()

    while left < right : 
        current_sum = arr[left] + arr[right]

        if current_sum == target : 
            result.append((left, right))
            left+=1
        elif current_sum < target : 
            left+=1
        else : 
            right-=1

    return result


if __name__ == '__main__' : 
    arr = [1,5,7,1]
    res = find_pairs(arr, 6)
    print(len(res))