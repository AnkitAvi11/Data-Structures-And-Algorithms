#   Smallest Difference Problem : Two arrays are given and you have to find the 
#   pair (i , j) such abs(i-j) is the smallest where i belongs to the first array and   j belong to the second array respectively

def smallestDifference(arr1 : list, arr2 : list) : 
    arr1.sort();arr2.sort()
    i = 0;j = 0

    smallest = float("inf");
    smallestPair = list()
    
    while i < len(arr1) and j < len(arr2) : 
        fnum = arr1[i];snum = arr2[j]
        
        if fnum < snum : 
            current = snum - fnum
            i += 1
        elif snum < fnum : 
            current = fnum - snum
            j += 1
        else : 
            return [fnum, snum]

        #   updating the smallest difference pair if found a new one
        if current < smallest : 
            smallest = current
            smallestPair = [fnum, snum]
            
    return smallestPair

if __name__ == '__main__' : 
    print(smallestDifference([12,3,45,6], [2,4,4,5]))
    