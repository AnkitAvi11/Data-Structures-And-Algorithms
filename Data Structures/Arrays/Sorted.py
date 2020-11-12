
def sorted_elements(arr : list) : 
    result = list()

    for el in arr : 
        if el not in result : 
            result.append(el)

    result.sort()
    return result


if __name__ == '__main__' : 
    result = sorted_elements([7,6,7,3,28,7])

    for el in result : 
        print(el, end = " ")