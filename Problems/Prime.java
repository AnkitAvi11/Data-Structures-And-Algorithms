import java.util.Scanner;

class PrimeCheck {
    public static boolean isPrime(int num) {

        if(num < 2) 
        return false;

        if (num==2)
        return true;

        for(int i = 2;i<=Math.sqrt(num);i++){
            if(num%i==0) {
                return false;
            }
        }

        return true;
    }

}

public class Prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int range = sc.nextInt();
        sc.close();

        for(int i=1;i<=range;i++){
            if(PrimeCheck.isPrime(i)) {
                System.out.print(i+":");
            }
        }
    }    
}
