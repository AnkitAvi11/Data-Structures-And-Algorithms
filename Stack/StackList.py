"""
Stack using linked list
"""

class Node : 

    def __init__(self, data) : 
        self.data = data
        self.next_node = None


class Stack : 
    
    def __init__(self) : 
        self.top = None
        

    
    def push(self, data) : 
        newNode = Node(data)

        if self.top is None : 
            self.top = newNode
        else :
            newNode.next_node = self.top
            self.top = newNode
        

    def pop(self) -> int : 
        if self.top is None : 
            return "Stack is empty"
        
        ptr = self.top 
        temp = ptr.data
        self.top = ptr.next_node
        del ptr
        return temp



if __name__ == '__main__' : 
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
        

