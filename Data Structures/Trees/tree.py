#   python program to implement tree

class Node : 
    def __init__(self, sk) : 
        self.val = sk
        self.right = None
        self.left = None


#   class for creating and traversing a tree
class Tree : 

    #   constructor for the class
    def __init__(self) : 
        self.root = None

    
    #   method to insert a node into the binary tree
    def insert(self, sk) : 
        if self.root is None : 
            self.root = Node(sk)
            return
        
        queue = list()
        queue.append(self.root)

        while queue : 
            temp = queue.pop(0)

            if temp.left is None :  
                temp.left = Node(sk)
                break
            else : 
                queue.append(temp.left)

            if temp.right is None : 
                temp.right = Node(sk)
                break
            else : 
                queue.append(temp.right)

    #   method to get the root of the tree
    def get_root(self) :
        return self.root


    #   method to traverse the entire tree (in order traversal)
    def traverse(self, root) : 
        if not root : 
            return

        self.traverse(root.left)
        print(root.val, end = " ")
        self.traverse(root.right)


    #   method to search a node in the tree
    def search(self, root, sk) : 
        if root is None : 
            return -1
        else : 
            pass


    #   method to delete a node from the tree
    """
    Algorithm : 
        1. Starting at root, find the deepest and the rightmost node in the binary tree and node which we want to delete
        2. Replace the deepest rightmost node's data with the node to be deleted
        3. Then delete the deepest rightmost node
    """
    def delete(self) : 
        pass


if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.traverse(tree.get_root())
    search = tree.search(tree.get_root(),3)
    if search == -1 : 
        print('Element was not found in the tree')
    else : 
        print("Element was found : {} node".format(search.val))