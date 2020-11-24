

def solve_candy(arr : list, k : int) -> int : 

    arr.sort()
    
    mid_element = arr[len(arr)//2-1] if len(arr) %2 == 0 else arr[len(arr)//2]
    mid_pos = (len(arr) // 2 - 1) if len(arr) %2 == 0 else len(arr) // 2

    count = 0

    for _ in arr[mid_pos:] :
        count+=1

    if count >= k : 
        return mid_element
    
    return -1


if __name__ == "__main__":
    print(solve_candy([26,20,23], 2))