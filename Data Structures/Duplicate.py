#   Find the duplicate in an array of N+1 integers.
#   Leetcode problem : 287

#   Takes O(n) time complexity and O(n) space complexity
def duplicate(arr) : 
    seen = list()

    for el in arr : 
        if el in seen : 
            return el
        else : 
            seen.append(el)

    return -1


#   Takes O(n) time complexity and O(1) space complexity
def duplicateNumber(arr) :
    slow, fast = arr[0], arr[0]

    slow = arr[slow]
    fast = arr[arr[fast]]

    while slow != fast :
        slow = arr[slow]
        fast = arr[arr[fast]]

    fast = arr[0]

    while slow != fast :
        slow = arr[slow]
        fast = arr[fast]

    return slow


if __name__ == '__main__' : 
    print(duplicateNumber([1,2,3,4,2]))
    print(duplicate([1,2,3,5]))

    