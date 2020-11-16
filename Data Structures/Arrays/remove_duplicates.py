"""
Geeks for geeks array problem : Write a program to remove duplicates from a sorted array
"""


def remove_duplicates(arr: list) : 
    res = set()

    for el in arr : 
        res.add(el)

    return list(res)


def find_duplicates(arr : list) : 
    result = list()

    for el in arr : 
        if el not in result : 
            result.append(el) # append, insert and extend

    return result


if __name__ == '__main__' : 
    print(find_duplicates([1,1,2,2,3,3,4,5]))