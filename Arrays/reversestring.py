"""
Write a function that takes a list of characters and reverses the letters in place
"""

def reverseCharacters(arr) : 
    left = 0;right=len(arr)-1

    while left<=right : 
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    chars = ['a','b','c','d', 'e']
    reverseCharacters(chars)
    print(chars)
    