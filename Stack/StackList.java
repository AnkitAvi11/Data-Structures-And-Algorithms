
class Node {
    int data;
    Node next;
    Node() {
        data = 0;
        next = null;
    }

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Stack {
    private Node top;

    public Stack() {
        this.top = null;
    }

    public void push(int data) {
        Node newNode = new Node(data);
        if(this.top == null) {
            this.top = newNode;
        }else{
            newNode.next = this.top;
            this.top = newNode;
        }
    }

    public int pop() {
        if(this.top == null) {
            return -1;
        }else{
            Node ptr = this.top;
            int data = ptr.data;
            this.top = ptr.next;
            ptr = null;
            return data;
        }
    }
}


public class StackList {
    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.print(stack.pop()+" ");
        System.out.print(stack.pop()+" ");
        System.out.print(stack.pop()+" ");
        System.out.print(stack.pop()+" ");
    }
}
