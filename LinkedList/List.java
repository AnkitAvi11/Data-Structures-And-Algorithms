
class Node {
    int data;
    Node next;
}


class LinkedList {

    private Node head;

    public LinkedList() {
        this.head = null;
    }

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

    public Node getHead() {
        return this.head;
    }

    public void recursiveTraversal(Node head) {
        if (head == null) {
            System.out.println("Printed all nodes");
            return;
        }

        System.out.print(head.data);
        this.recursiveTraversal(head.next);
    }
    
}


class List {
    public static void main(String[] args) {
        LinkedList ob = new LinkedList();
        ob.append(1);
        ob.append(2);
        ob.append(3);
        ob.recursiveTraversal(ob.getHead());
    }
}