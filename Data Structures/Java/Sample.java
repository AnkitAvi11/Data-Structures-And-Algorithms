
/**
 *      POINTS TO BE NOTED
 *      1. There can't be more than one public class in a file
 *      2. If there is a public class in the file then the file name must match the class name
 *      3. Static members are only accessible by static methods
 *      
 *      CONTROL FLOW
 *      1. if statements
 *      2. if - else or if else if ladder
 *      3. switch
 * 
 *      
 *      1. Program to find the min and max in a given array, using a single loop   (15mins)
 *      2. Program to nth smallest number in an array (1hr)
 * 
 */





import java.util.Scanner;
import java.util.Arrays;
import factorial.Factorial;

public class Sample {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        Factorial ob = new Factorial();
        System.out.println("Factorial of 5 = " + ob.calculateFactorial(5));
    }

}




