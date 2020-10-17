
def minMax(arr : list) : 

    min,max = arr[0], arr[0]

    for el in arr : 
        if el < min : 
            min = el

        if el > max : 
            max = el

    return (min, max)

if __name__ == "__main__":
    print(minMax([1,2,3,4,5,6]))
