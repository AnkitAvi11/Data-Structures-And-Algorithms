"""
Your company built an in-house calendar tool called hiCal. You want to add a feature to see the times in a day when everyone is available.
"""

def hiCal(arr : list) -> list : 
    result = list()

    for i in range(len(arr)-1) : 
        for j in range(i+1, len(arr)) : 
            
            if arr[j][0] <= arr[i][0] <= arr[j][1] or arr[j][0] <= arr[i][1] <= arr[j][1] or arr[i][0] <= arr[j][0] <= arr[i][1] or arr[i][0] <= arr[j][1] <= arr[i][1] : 
                print('came here')
                result.append((min(arr[i][0], arr[j][0]), max(arr[i][1], arr[j][1])))

    return result


if __name__ == '__main__' : 
    print(hiCal([(5,8),(1,4),(6,8)]))