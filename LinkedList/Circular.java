class Node {
    int data;
    Node next;

    public Node () {}

    public Node (int sk) {
        this.data = sk;
        this.next = null;
    }
}

class CircularLinkedList {

    private Node head;    

    public CircularLinkedList() {
        this.head = null;
    }

    public void append(int data) {
        Node newNode = new Node(data);
        if (this.head == null) {
            this.head = newNode;
            newNode.next = this.head;
        }else{
            Node ptr = this.head;
            while(ptr.next != this.head) ptr=ptr.next;
            ptr.next = newNode;
            newNode.next = this.head;
        }
    }

    public void traverse() {
        if (this.head == null) {
            System.out.println("The linked list is empty");
            return;
        }

        Node ptr = this.head;
        while(ptr.next != this.head) {
            System.out.print(ptr.data + " : ");
            ptr = ptr.next;
        }
        System.out.print(ptr.data);
    }

}

public class Circular {
    public static void main(String[] args) {
        CircularLinkedList ob = new CircularLinkedList();
        ob.append(1);
        ob.append(2);
        ob.append(3);
        ob.traverse();
    }
}