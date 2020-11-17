
#   structure to create a node for the linked list
class Node : 
    data = None 
    next_node = None



class LinkedList : 

    #   cosntructor of the program
    def __init__(self) : 
        self.head = None


    #   method to append a new node at the end of the list
    def append(self, sk) : 
        ptr = Node()
        ptr.data = sk
        ptr.next_node = None

        if self.head is None : 
            self.head = ptr

        else : 
            qptr = self.head
            while qptr.next_node is not None : qptr = qptr.next_node
            qptr.next_node = ptr



    #   iterative method to traverse the linked list
    def traverse(self) : 
        ptr = self.head
        if self.head is None : 
            print("List is empty")
        else : 
            ptr = self.head 
            while ptr is not None : 
                print(ptr.data, end = " : ")
                ptr = ptr.next_node

    
    #   recursive method to traverse the linked list
    def recursive_traversal(self, head) : 
        if head is None : 
            return print("list printed successfully. no data left to display.")

        print(head.data, end = " ")
        return self.recursive_traversal(head.next_node)

    #   method to return the main node
    def returnhead(self) : return self.head
    
    #   method to count the number of nodes in the linked list
    def return_number_of_nodes(self) -> int: 
        total_nodes = 0
        ptr = self.head

        while ptr is not None : 
            total_nodes += 1
            ptr = ptr.next_node

        return total_nodes

if __name__ == '__main__' : 
    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.recursive_traversal(linkedlist.returnhead())
    print("total number of nodes = {}".format(linkedlist.return_number_of_nodes()))

