/**
 * Write a function to sort the array using selection sort
 * -------------------------------------------------------
 * [5,3,1,6,2] - ascending order (1)
 * 
 * [1,3,3,5,6,2] (2)
 * 
 * [1,2,5,6,3] (3)
 * 
 * [1,2,3,5,6]
 * 
 */

public class Selection {

    static void selectionSort(int[] arr) {

        for(int i=0;i<arr.length-1;i++) {
            int smallest = arr[i], pos = i;

            for(int j = i+1;j<arr.length;j++) {
                if (arr[j] < smallest) {
                    smallest = arr[j];
                    pos = j;
                }
            }

            //  swapping
            int temp = arr[i];
            arr[i] = arr[pos];
            arr[pos] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {5,3,1,6,2};
        selectionSort(arr);
        for(int x : arr) 
            System.out.println(x + " : ");
    }
}
