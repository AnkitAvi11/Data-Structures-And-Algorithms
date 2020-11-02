
"""
PROGRAM TO CREATE A LINKED LIST IN PYTHON
"""

#   class used to create a single node or point to node
class Node : 
    data = None
    next_node = None


#   class to create a linked list
class LinkedList : 

    def __init__(self) : 
        self.head = None


    #   function to insert a node at the end of the linked list    
    def insertData(self, num) : 
        ptr = Node()
        ptr.data = num
        ptr.next_node = None
        
        if self.head == None : 
            self.head = ptr
        else : 
            qptr = self.head
            while qptr.next_node != None : 
                qptr = qptr.next_node

            qptr.next_node = ptr

    

    #   function to traverse the entire linked list (iterative method)
    def traverse(self) :
        if self.head == None : 
            print("No data in the list")
        else : 
            ptr = self.head
            while ptr != None : 
                print(ptr.data, end = " -> ") 
                ptr = ptr.next_node



    #   function to get the head pointer
    def gethead(self) :
        return self.head


    #   function to traverse a linked list recursively
    def recursiveTraverse(self, main_node) : 
        if main_node == None : 
            print("list ended")
            return

        print(main_node.data)
        self.recursiveTraverse(main_node.next_node)


    
    #   function to delete a node from the linked list using the data
    def remove(self, sk) : 
        if self.head == None : 
            print("The lis is empty")
            return

        if self.head.data == sk : 
            ptr = self.head
            self.head = ptr.next_node
            del ptr
            print("Element deleted")
            return

        qptr = self.head 
        
        while qptr.next_node != None : 

            if qptr.next_node.data == sk : 
                ptr = qptr.next_node
                qptr.next_node = ptr.next_node
                del ptr
                print("Element deleted ")
                return


            qptr = qptr.next_node

        print("Element was not found")       
        

    #   searching an element in the linked list
    def searchNode(self, sk) : 
        ptr = self.head
        if ptr is None : 
            print("List is empty");return

        while ptr is not None : 
            if ptr.data == sk : 
                print("Element was found in the list")
                return
            ptr = ptr.next_node

        print("Element was not found in the list")



    #   deleting the first node from the list
    def deleteFirst(self) : 
        if self.head is None : 
            print("list is empty")
            return

        ptr = self.head
        self.head = ptr.next_node
        num = ptr.data
        del ptr
        print("Deleted the first node")
        return num

    

    #   function to delete duplicate nodes from the linked list
    def delDuplicate(self) : 
        dup = set()
        if self.head is None : 
            print("List is empty")
            return

        ptr = self.head;prev=self.head

        dup.add(ptr.data)
        ptr = ptr.next_node

        while ptr is not None : 
            if ptr.data in dup : 
                prev.next_node = ptr.next_node
                del ptr
                ptr = prev.next_node
            else : 
                dup.add(ptr.data)
                prev = ptr
                ptr = ptr.next_node

            



if __name__ == '__main__' : 

    mylist = LinkedList()
    mylist.insertData(5)
    mylist.insertData(4)
    mylist.insertData(3)
    mylist.insertData(2)
    mylist.insertData(5)  

    mylist.traverse()

    print()
    mylist.delDuplicate()  

    mylist.traverse()


