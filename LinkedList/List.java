
//  Data structure to create node of the linked list
class Node {
    int data;
    Node next;
}


class LinkedList {

    private Node head;

    //  constructor of the linked list class
    public LinkedList() {
        this.head = null;
    }

    //  method to append a node at the end of the linked list
    public void append(int sk) {

        Node ptr = new Node();
        ptr.data = sk;
        ptr.next = null;

        if (this.head == null) this.head=ptr;
        else {
            Node qptr = this.head;
            while (qptr.next != null) qptr=qptr.next;
            qptr.next = ptr;
        }

    }


    //  iterative method to traverse all the nodes of the linked list
    public void traverse() {

        Node ptr = this.head;
        if (ptr == null) {
            System.out.println("Linked list is empty");
            return;
        }
        while(ptr!=null) {
            System.out.println(ptr.data + " : ");
            ptr = ptr.next;
        }

    }

    //  method to return the head node of the linked list
    public Node getHead() { return this.head; }

    //  recursive method to traverse all the nodes of the linked list 
    public void recursiveTraversal(Node head) {

        if (head == null) {
            System.out.println("Printed all nodes");
            return;
        }

        System.out.print(head.data);
        this.recursiveTraversal(head.next);

    }

    //  method to count the number of nodes in the linked list
    public long countNodes() {
        Node ptr = this.head;
        long count = 0;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        return count;
    }

    //  method to calculate the sum of all the nodes in the linked list
    public long sum(Node head) {
        if (head == null) return 0;
        return head.data + sum(head.next);
    }

    //  method to get maximum
    public int getmax(int m, int n) {
        return m > n ? m : n;
    }

    //  method to get the maximum element from the linked list
    public int max() {

        if(this.head == null) return 0;

        int largest = this.head.data;
        Node ptr = this.head;

        while(ptr!=null) {
            largest = this.getmax(largest, ptr.data);ptr=ptr.next;
        }

        return largest;

    }

    public int search(int sk) {
        Node ptr = this.head;
        while(ptr!=null) {
            if(ptr.data == sk) {
                return ptr.data;
            }
            ptr = ptr.next;
        }
        return -1;
    }

    public boolean isAscending() {
        Node ptr = this.head;
        while(ptr.next!=null) {
            if(ptr.data > ptr.next.data) {
                return false;
            }
            ptr = ptr.next;
        }
        return true;
    }
    
}


class List {
    public static void main(String[] args) {
        LinkedList ob = new LinkedList();
        ob.append(1);
        ob.append(2);
        ob.append(3);
        ob.recursiveTraversal(ob.getHead());
        System.out.println("Total number of nodes = "+ob.countNodes());
        System.out.println("Sum of nodes of the list = "+ob.sum(ob.getHead()));
        System.out.println("Maximum element in the linked list = " + ob.max());
    }
}