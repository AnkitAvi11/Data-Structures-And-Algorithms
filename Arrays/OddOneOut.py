#   Odd one out from hackerearth solution

def oddOneOut(arr : list) : 
    n = len(arr)
    arr.sort()
    summation = sum(arr)

    actual_sum = int((n+1)/2 * (2*arr[0] + (n*2)))
    print(actual_sum)
    return actual_sum - summation


if __name__ == '__main__' : 
    arr = list(map(int, input("Enter the elements into the array : ").split()))
    print(oddOneOut(arr))