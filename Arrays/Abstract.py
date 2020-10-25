from abc import ABC, abstractmethod

class AbstractClass(ABC) : 

    @abstractmethod
    def myabstractMethod(self) : 
        pass


    
if __name__ == '__main__' :

    arr = [1,2,3,4,5,6,7]
    print(len(arr))
    print(arr.count(1))


