
"""

Implementing circular linked list 

"""

#   class to create a node of the linked list
class LinkedlistNode : 
    def __init__(self, data) : 
        self.data = data
        self.next_node = None


#   circular linked list class (main class)
class CircularList : 

    #   constructor of the class
    def __init__(self) : 
        self.head = None


    #   method to append a node at the end of the circular linked list
    def append(self, data) : 

        ptr = LinkedlistNode(data)
        
        if self.head is None : 
            self.head = ptr
            ptr.next_node = self.head

        else : 

            qptr = self.head
            while qptr.next_node != self.head : qptr = qptr.next_node

            qptr.next_node = ptr
            ptr.next_node = self.head


    #   method to traverse the circular linked list
    def traverse(self) : 
        if self.head is None : 
            print('The linked list is empty')
            return

        else : 
            ptr = self.head
            while ptr.next_node != self.head : 
                print(ptr.data, end = " : ")
                ptr = ptr.next_node
            print(ptr.data)


    #   method to search for a element in the linked list
    def search(self, sk) : 
        if self.head is None : 
            return False
        
        if self.head.data == sk : 
            return True

        ptr = self.head.next_node

        while ptr != self.head : 
            if ptr.data == sk : 
                return True

            ptr = ptr.next_node

        return False


    #   method to delete the given node from the linked list
    def delete(self, sk) :
        if self.head is None : 
            print('Linked list empty')
            return
        
        if self.head.data == sk : 

            #   if the given node is the first node to be deleted
            qptr = self.head
            ptr = self.head 

            while ptr.next_node != self.head : ptr = ptr.next_node

            self.head = qptr.next_node
            ptr.next_node = self.head
            del qptr
            
        else : 

            #   deleting any other node from apart from the first node
            ptr = self.head
            qptr = self.head.next_node

            while qptr.next_node != self.head : 
                if qptr.data == sk : 
                    ptr.next_node = qptr.next_node
                    del qptr
                    return
                    
                ptr = qptr
                qptr = qptr.next_node

            if qptr.data == sk : 
                ptr.next_node = self.head
                del qptr


if __name__ == '__main__' : 
    linkedList = CircularList()

    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)

    linkedList.traverse()

