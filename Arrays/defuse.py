#   defuse the bomb problem leetcode biweekly challenge

def defuse_bomb(arr : list, k : int) -> None : 
    res = list()
    if k == 0 :
        for i in range(len(arr)) : 
            arr[i] = 0
        return arr

    elif k > 0 : 
        for i in range(len(arr)) : 
            cum = 0
            j = 1;pos=i+1
            while j <= k : 
                if pos == len(arr) : pos=0
                cum += arr[pos]
                pos+=1
                j+=1
            res.append(cum)
        return res
    else : 
        for i in range(len(arr)) : 
            cum = 0 
            j=1;pos=i-1;
            while j<=abs(k) : 
                if pos == -1 : pos = len(arr)-1
                cum += arr[pos]
                pos-=1
                j+=1
            
            res.append(cum)

        return res

if __name__ == "__main__":
    arr = [2,4,9,3];k=-2
    arr = defuse_bomb(arr, k)
    print(arr)
