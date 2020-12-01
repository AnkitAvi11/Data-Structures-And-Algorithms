"""
Circular queue using linked list
"""

#   Node class used for creating individual nodes
class Node : 
    def __init__(self, sk) : 
        self.val = sk
        self.next = None


#   class used to create the linked list 
class CircularQueue : 
    #   constructor of the class
    def __init__(self) : 
        self.rear = None
        self.front = None


    #   method to insert a node into the queue
    def insert(self, sk) : 
        new_node = Node(sk)
        if self.rear is None : 
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        else : 
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node         
    

    #   method to traverse the linked list
    def traverse(self) : 
        ptr = self.front
        if ptr is None : 
            print("Queue is empty")
            return
        else : 
            while ptr != self.rear : 
                print(ptr.val, end = " ")
                ptr = ptr.next

            print(ptr.val, end = " ")

    
    #   method to delete a node from the queue linked list
    def delete(self) : 
        ptr = self.front 
        if self.front is None : 
            return "Queue is empty"
        
        if self.front == self.rear : 
            temp = self.front.val
            self.front = None
            self.rear = None
            return temp
        else : 
            temp = ptr.val
            self.front = self.front.next
            self.rear.next = self.front
            del ptr
            return temp


#   driver code for the program
if __name__ == "__main__":
    queue = CircularQueue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())

    
    

    