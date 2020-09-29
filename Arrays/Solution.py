
#   program to find the number which occurs for the maximum number of times
#   in an array

def maxTimes(arr : list) : 
    result = dict()

    for el in arr : 
        if el in result : 
            result[el] += 1
        else :
            result[el] = 1

    count = max([x for x in result.values()])

    if count == 1 : 
        return -1
    else : 
        return result[count]


if __name__ == '__main__' : 
    print(maxTimes([1,2,3,4,5]))