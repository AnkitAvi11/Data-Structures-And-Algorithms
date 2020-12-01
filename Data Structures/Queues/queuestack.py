#   Python program to implement a queue using two stacks

class Queue : 

    def __init__(self) : 
        #   for insertion
        self.stack1 = list()
        #   for deletion
        self.stack2 = list()


    def insert(self, sk): 
        self.stack1.append(sk)


    def delete(self) : 
        if self.stack2 : 
            return self.stack2.pop()
        else : 
            if self.stack1 : 
                while self.stack1 : 
                    self.stack2.append(self.stack1.pop())

                return self.stack2.pop()
        
            else : 
                return ("Queue is empty")

    def traverse(self) : 
        print(self.stack1)       
        print(self.stack2)


if __name__ == "__main__":
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    print(queue.delete())
    queue.insert(4)
    queue.traverse()

    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
