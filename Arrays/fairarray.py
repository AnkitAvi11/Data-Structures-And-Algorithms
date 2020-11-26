
#   fair array leetcode weekly challenge solution

def clac_odd_even (arr : list) : 
    odd = 0;even = 0

    for i in range(len(arr)) : 
        if i%2 == 0 : 
            even += arr[i]
        else : 
            odd += arr[i]

    return (odd, even)


def fair_array(arr : list) -> int : 
    count = 0

    for i in range(len(arr)) : 
        odd, even = clac_odd_even(arr)
        
        if i%2 == 0 : 
            if even - arr[i] == odd : 
                count+=1

        else : 
            if even == odd-arr[i] : 
                count+=1

    return count


if __name__ == "__main__":
    print(fair_array([6,1,7,4,1]))