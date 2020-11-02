#   operator overloading in python
from abc import ABC, abstractmethod

class OperatorOverloading(ABC) : 

    @abstractmethod
    def __add__(self) : pass


class Overloaded(OperatorOverloading) : 

    def __init__(self, num) : 
        self.num = num
            
    def __add__(self) : 
        pass
    pass

class Overloading : 

    def __init__(self, num) : 
        self.num = num


    #   relational operator overloading
    def __le__(self, other) : 
        return self.num <= other.num

    def __lt__(self, other) : 
        return self.num < other.num

    def __ge__(self, other) : 
        return self.num >= other.num

    def __gt__(self, other) :
        return self.num > other.num


    #   basic multiplication methods
    def __floordiv__(self, other) : 
        return self.num // other.num

    def __truediv__(self, other) : 
        return self.num / other.div

    def __mul__(self, other) : 
        return self.num + other.num

    def __add__(self, other) : 
        return self.num + other.num

    def __sub__(self, other) : 
        return self.num + other.num


if __name__ == '__main__' : 
    ob = Overloading(10)
    ob1 = Overloading(20)

    print(ob//ob1)