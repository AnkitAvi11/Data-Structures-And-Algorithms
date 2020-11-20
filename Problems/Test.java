
import java.util.*;

class Test {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers : ");
        int m = sc.nextInt();
        int n = sc.nextInt();

        try {
            System.out.println("The quotient of "+m+" / "+" n = "+(m/n));
        }
        catch(ArithmeticException exception) {
            System.out.println(exception.toString());
        }
        finally{
            System.out.println("Inside the finally block");
        }

        sc.close();
    }
}