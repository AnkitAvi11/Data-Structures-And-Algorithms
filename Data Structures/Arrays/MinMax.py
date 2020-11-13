
def min_mix (arr) : 
    min = arr[0];max=arr[0]

    for el in arr : 
        if el < min : 
            min = el
        if el > max : 
            max = el

    return (min, max)



if __name__ == '__main__' : 
    print(min_mix([1,2,3,4,5]))