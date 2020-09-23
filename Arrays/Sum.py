class Solution : 

    def __init__(self, arr) : 
        self.arr = arr

    def sum(self) -> int : 
        s = 0
        for el in self.arr : 
            s += el
        return s


if __name__ == '__main__' : 
    ob = Solution([1,2,3,4,5])
    print(ob.sum())