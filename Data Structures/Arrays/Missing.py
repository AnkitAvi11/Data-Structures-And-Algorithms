#   Find the Missing and Repeating Number

def missingNumber(arr) : 

    visited = [0 for _ in range(len(arr)+1)]

    repeated_element = -1
    
    for el in arr : 
        if visited[el] == 0 : 
            visited[el] = el
        else : 
            repeated_element = el

    print(visited)
    return [repeated_element, abs(sum(visited) - sum([i for i in range(1,len(arr)+1)]))]


if __name__ == '__main__' : 
    print(missingNumber([1,2,3,4,1,5,7]))