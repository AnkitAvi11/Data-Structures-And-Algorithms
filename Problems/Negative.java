/**
 * Move all the negative elements towards the left of the right
 * arr = [-1, 1,2, 3,-5,6,7,8-10]
 * 
 * temp = -1
 * 
 * output = [-1,-5,-10,1,2,3,6,7,8] 
 */

public class Negative {

    public static void moveNegative(int[] arr) {
        int j, temp;

        for(int i=1;i<arr.length;i++){
            temp = arr[i];
            j=i-1;
            while (j>=0 && temp < 0) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {89, 10,-1,-2,-5,11,67};
        moveNegative(arr);
        for(int x : arr) 
            System.out.println(x + " : ");
    }
}
