#   lonely solution from geeksforgeeks

from collections import Counter

def get_lonely(arr : list, k : int) : 

    counter = Counter(arr)


    for key, value in counter.items() : 
        if value != k : 
            return key

    return -1


if __name__ == '__main__' : 
    print(get_lonely([1 ,8 ,7 ,2 ,1, 7 ,1 ,8 ,7,8], 3))
