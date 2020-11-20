"""
Python program to find the smallest positive number missing from the array
"""

def find_missing(arr : list) : 

    has_seen = list()

    for el in arr : 
        if el >= 0 : 
            has_seen.append(el)


    for i in range(len(has_seen)-1) : 
        if has_seen[i+1]-has_seen[i] != 1 : 
            return has_seen[i+1] - has_seen[i]

    return has_seen[len(has_seen)-1] + 1

    


if __name__ == "__main__":
    print(find_missing([1,2,3,4,5]))
