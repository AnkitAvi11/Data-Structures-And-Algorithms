
#   class node to create a node for the queue linked list
class Node : 

    def __init__(self, val) : 
        self.val = val
        self.next = None


class Queue : 

    #   contructor of the queue class
    def __init__(self) : 
        self.front = None
        self.rear = None


    #   method to insert an element into the queue
    def insert(self, val) : 
        new_node = Node(val)

        #   if the front and rear pointer are null by default
        if self.rear is None and self.front is None : 
            self.rear = new_node
            self.front = new_node

        #   when there is already one more nodes or elements in the queue
        else : 
            self.rear.next = new_node
            self.rear = new_node


    def traverse(self) : 
        ptr = self.front
        if ptr is None : 
            print('Queue is empty')
            return
        else : 
            while ptr is not None : 
                print(ptr.val, end = " ")
                ptr = ptr.next       


    def delete(self) : 
        ptr = self.front
        if ptr is None : 
            print("queue is empty")
            return
        else : 
            print(ptr.val)
            self.front = ptr.next
            del ptr


if __name__ == '__main__' : 
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.delete()
    queue.delete()
    queue.delete()
    queue.delete()
    queue.traverse()