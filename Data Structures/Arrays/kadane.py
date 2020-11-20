#   kadanes' algorithms

def max_contiguos_sum(arr : list) : 
    sum_so_far = -9999;current_sum = 0

    for el in arr : 
        current_sum+=el

        if current_sum > sum_so_far : 
            sum_so_far = current_sum

        if current_sum < 0 : 
            current_sum = 0 

    return sum_so_far
    

if __name__ == "__main__":
    print(max_contiguos_sum([-1,-2,-3,-4]))
    