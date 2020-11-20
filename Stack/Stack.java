
class StackClass {
    private int[] arr;
    private int top;

    public StackClass() {
        this.arr = new int[5];
        this.top = -1;
    }


    public void push(int sk) {

        try{

            if(this.top == this.arr.length-1) {
                System.out.println("Stack is overflow");
                return;
            }
    
            this.top++;
            this.arr[top] = sk;
    
            System.out.println("Element inserted into the stack");

        }catch(ArrayIndexOutOfBoundsException exception) {
            System.out.println(exception.toString());
        }catch(Exception exception) {
            System.out.println(exception.toString());
        }
        
    }


    public int pop() {
        if(top==-1) {
            System.out.println("Stack is empty/underflow");
            return -1;
        }
        return this.arr[this.top--];
    }

    public int peek() {
        return this.top;
    }

    public boolean isFull() {
        if(this.top == this.arr.length) {
            return true;
        }
        return false;
    }

    public boolean isEmpty() {
        return this.top == -1 ? true : false;        
    }

    public void traverse() {
        if(this.isEmpty()) {
            System.out.println("Stack is empty");
            return;
        }
        for(int i=0;i<=this.top;i++)
            System.out.print(this.arr[i] + " ");
    }

}

public class Stack {
    public static void main(String[] args) {
        StackClass ob = new StackClass();

        ob.push(1);
        ob.push(2);
        ob.push(3);
        ob.push(4);
        ob.push(5);
        ob.push(6);

        ob.traverse();
    }
}