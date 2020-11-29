class CreateQueue {

    private int[] arr;
    private int front, rear;

    public CreateQueue() 
    {
        this.arr = new int[5];
        this.front = this.rear = -1;
    }

    public void insert(int sk)
    {
        if(this.front == -1 && this.rear == -1) 
        {
            this.front = this.rear = 0;
        }

        //  overflow condition for the queue
        if(this.rear == this.arr.length)
        {
            System.out.println("Queue overflow");
            return;
        }

        //  when the queue is empty or has space in it
        this.arr[rear++] = sk;

    }

    public void traverse() 
    {
        if(this.front==-1) {
            System.out.println("Queue underflow");
            return;
        }
        for(int i = this.front;i<this.rear;i++) {
            System.out.print(this.arr[i]+ " : ");
        }
    }

    public int delete() 
    {
        if(this.front == this.rear || this.front == -1) {
            System.out.print("Queue underflow");
            return -1;
        }
        return this.arr[this.front++];
    }

}


public class Queue {

    public static void main(String[] args) 
    {
        CreateQueue queue = new CreateQueue();
        queue.insert(1);
        queue.insert(2);
        queue.insert(3);
        queue.insert(3);
        queue.insert(3);
        System.out.println(queue.delete());
        System.out.println(queue.delete());
        System.out.println(queue.delete());
        System.out.println(queue.delete());
        System.out.println(queue.delete());
        System.out.println(queue.delete());
        queue.traverse();
    }

}