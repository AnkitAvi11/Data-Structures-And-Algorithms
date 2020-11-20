"""

Kadane's algorithm 
to find the sub array with maximum sum

"""


def kadane_algorithm(arr : list) : 
    sum_so_far = -9999; current_sum = 0

    for i in range(len(arr)) : 
        current_sum += arr[i]

        if current_sum > sum_so_far : 
            sum_so_far = current_sum

        if current_sum < 0 : 
            current_sum = 0
        
    return sum_so_far

if __name__ == "__main__":
    print(kadane_algorithm([-1,-2,-3,-4]))
