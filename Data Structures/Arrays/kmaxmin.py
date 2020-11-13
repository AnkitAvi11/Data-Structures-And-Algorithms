#   find the kth min and max element of an array given that all the elements of the array are distinct
#   expected complexity : O(n)

def kth_min_max(arr: list, k: int) : 
    arr.sort()
    print(arr)
    return (arr[k-1], arr[len(arr)-k])


if __name__ == "__main__":
    print(kth_min_max([7,10,4,20,15], 4))

