#   Leetcode ugly number III

def nthUglyNumber(n : int, a : int, b : int, c : int) -> int : 
    smallest_number = min(a,min(b,c))

    i = smallest_number

    while i <= n : 
        i+=smallest_number

    return i


if __name__ == '__main__' : 
    print(nthUglyNumber(1000000000,2,217983653,336916467))