#   Program to reverse an array 

def reverseArray(arr : list) : 

    for i in range(len(arr) // 2) : 
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    reverseArray(arr)
    print(arr)
