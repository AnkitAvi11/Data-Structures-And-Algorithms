#   Inflight entertainment
#   This algorithm takes O(n) time complexity and o(n) space complexity

def flight_entertainment(arr : list, target : int) -> bool : 
    #   movie already been seen
    has_seen = set()

    for el in arr : 
        second_movie_length = target - el 

        if second_movie_length in has_seen : 
            return True
        
        has_seen.add(el)

    return False


#   this algorithm takes O(nlogn) time complexity and O(1) space complexity
def flight_movies(arr : list, target : int) -> bool : 
    left = 0;right = len(arr) - 1
    arr.sort()

    while left < right : 
        csum = arr[left] + arr[right]
        if csum == target : 
            return True
        elif csum < target : 
            left+=1
        else : 
            right =- 1

    return False


if __name__ == "__main__":
    print(flight_entertainment([1,2,1,4,5,6], 4))