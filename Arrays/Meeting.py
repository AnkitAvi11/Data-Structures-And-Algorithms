"""
Your company built an in-house calendar tool called hiCal. You want to add a feature to see the times in a day when everyone is available.
"""

def hiCal(arr : list) -> list : 
    #   sorting by the order of start time
    arr.sort()

    merged_meetinds = [arr[0]]

    for current_start_time, current_end_time in arr[1:] : 
        last_start_time, last_end_time = merged_meetinds[-1]

        if current_start_time <= last_end_time :
            merged_meetinds[-1] = (last_start_time, max(current_start_time, last_end_time))

        else : 
            merged_meetinds.append((current_start_time, current_end_time))
    

    return merged_meetinds

if __name__ == '__main__' : 
    print(hiCal([(5,8),(1,4),(6,8)]))