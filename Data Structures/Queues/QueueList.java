
class Node {
    protected int val;
    protected Node next;

    public Node () {
        this.val = 0;
        this.next = null;
    }

    public Node(int sk) {
        this.val = sk;
        this.next = null;
    }
}

class Queue{
    private Node front, rear;

    public Queue() {
        this.front = null;
        this.rear = null;
    }

    public void insert(int sk) {
        Node newnode = new Node(sk);
        if (this.rear == null) {
            this.front = this.rear = newnode;
        }
        else{
            this.rear.next = newnode;
            this.rear = newnode;
        }
    }

    public void traverse() {
        if(this.front == null) {System.out.println("Queue is empty");}
        Node ptr = this.front;
        while (ptr!=null) {
            System.out.print(ptr.val + " ");
            ptr = ptr.next;
        }
    }

    public int delete() {
        if(this.front == null) {
            System.out.println("Queue is empty");
            return -1;
        }
        Node ptr = this.front;
        this.front = ptr.next;
        int temp = ptr.val;
        ptr = null;
        return temp;
    }
}


public class QueueList {
    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.insert(1);
    }
}
