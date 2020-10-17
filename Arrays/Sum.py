
from abc import ABC, abstractclassmethod, abstractmethod

class AbstractClass(ABC) : 
    @abstractmethod
    def myabstractmethod(self) : 
        pass

class MyClass : 

    def __iter__(self) : 
        self.num = 0
        return self

    def __next__(self) : 
        if self.num < 10 : 
            self.num += 1
        else : 
            raise StopIteration

        return self.num

import os

if __name__ == '__main__' : 
    # ob = MyClass()
    # for el in ob : 
    #     print(el)
    os.chdir("../")
    print(os.listdir())

