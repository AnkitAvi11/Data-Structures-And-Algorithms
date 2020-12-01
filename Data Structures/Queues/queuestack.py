#   Python program to implement a queue using two stacks

class Node : 
    def __init__(self, sk) :
        self.val = sk
        self.next = None


class Stack : 
    #   constuctor for the class
    def __init__(self) : 
        self.top = None

    def __str__(self) : 
        string = ""
        ptr = self.top
        if ptr is not None : 
            while ptr is not None : 
                string+=str(ptr.val)
                ptr = ptr.next
            return string
        else : 
            return ""


    #   method to push node into the stack
    def push(self, sk) : 
        new_node = Node(sk)
        if self.top is None : 
            self.top = new_node
        else : 
            new_node.next = self.top
            self.top = new_node
        

    
    #   method to pop elements from the stack
    def pop(self) : 
        if self.top is None : 
            return "Stack is empty"
        
        ptr = self.top
        self.top = ptr.next
        temp = ptr.val
        del ptr
        return temp

    #   method to check if the stack is empty or not
    def isEmpty(self) : 
        if self.top is None : 
            return True
        return False



class Queue : 

    def __init__(self) : 
        #   for insertion
        self.stack1 = Stack()
        #   for deletion
        self.stack2 = Stack()


    def insert(self, sk): 
        self.stack1.push(sk)


    def delete(self) : 
        if not self.stack2.isEmpty() : 
            return self.stack2.pop()
        else : 
            if not self.stack1.isEmpty() : 
                while not self.stack1.isEmpty() : 
                    self.stack2.push(self.stack1.pop())

                return self.stack2.pop()
        
            else : 
                return ("Queue is empty")

    def traverse(self) : 
        print(self.stack1)       
        print()
        print(self.stack2)


if __name__ == "__main__":
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    print(queue.delete())
    queue.traverse()
    queue.insert(4)
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
