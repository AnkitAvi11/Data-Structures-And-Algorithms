"""

PYTHON PROGRAM TO IMPLEMENT DOUBLY LINKED LIST

"""

class Node : 
    data = None
    next_node = None
    prev_node = None


class DoublyLinkedList : 

    def __init__(self) : 
        self.head = None



    #   function to add a node into the doubly linked list
    def insertNode(self, sk) : 
        ptr = Node()
        ptr.data = sk
        ptr.next_node = None

        if self.head is None : 
            ptr.prev_node = None
            self.head = ptr

        else : 
            qptr = self.head
            while qptr.next_node is not None : qptr=qptr.next_node

            qptr.next_node = ptr
            ptr.prev_node = qptr

    

    #   function to traverse the entire doubly linked list
    def traverse(self) : 
        if self.head is None : 
            print("list is empty")
            return

        ptr = self.head
        while ptr is not None :
            print(ptr.data, end=" ")
            ptr = ptr.next_node    

    

if __name__ == '__main__' : 
    mylist = DoublyLinkedList()
    mylist.insertNode(1)
    mylist.insertNode(2)
    mylist.insertNode(3)

    mylist.traverse()

