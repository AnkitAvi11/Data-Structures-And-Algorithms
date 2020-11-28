#   queue using arrays in python

class Queue : 

    def __init__(self) : 
        self.arr = list()
        self.front = -1
        self.rear = -1


    def insert(self, sk) : 
        if self.front == -1 and self.rear == -1 : 
            self.front = 0
            self.rear = 0 

        if self.arr : 
            self.arr.append(sk)
            self.rear = len(self.arr) - 1

    
    def isEmpty(self) : 
        return self.rear == -1 or self.front == -1

    def peek(self) : 
        if self.rear == -1 : 
            return -1

        return self.arr[self.rear]

    def delete(self) : 
        if self.arr : 
            return self.arr[self.front]
        return -1

    def traverse(self) : 
        if self.arr : 
            for el in self.arr : 
                print(el, end=" ")
        return -1
        

if __name__ == "__main__":
    queue = Queue()
    