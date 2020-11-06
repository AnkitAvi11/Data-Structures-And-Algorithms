
#   capgemini solution

def solution(arr : list) : 
    left = list();right=list();
    length = len(arr)

    i = 0
    max_sum = -99999
    while length >= len(arr) // 2 : 
        
        left = arr[i:i+length//2]
        right = arr[::-1][:length//2]
        length-=1
        i+=1
        
        c_sum = 0
        for j in range(len(left)) : 
            c_sum+= left[j]*right[j]

        if c_sum >  max_sum  : 
            max_sum = c_sum

    return max_sum


if __name__ == '__main__' : 
    arr = list(map(int, input().split()))
    print(solution(arr))