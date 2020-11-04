
from collections import Counter

def thanosProblem(arr) : 

    counter = Counter(arr)

    max_val = -999999

    for key in counter.keys() : 
        if max_val < counter[key] : 
            max_key = key
            max_val = counter[key]

    del counter[max_key]

    return sum(counter)

if __name__ == '__main__' : 
    print(thanosProblem([3,3,2,2,2,2,1,3]))
