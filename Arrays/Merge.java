
import java.util.ArrayList;
import java.util.*;

public class Merge {

    public static int[] mergeArrays(int[] arr1, int[] arr2) {
        int i=0, j=0;

        int[] temp_arr = new int[arr1.length+arr2.length];

        for(;i<arr1.length;i++){
            if(arr1[i] > arr2[j]) {
                int temp = arr1[i];
                arr1[i] = arr2[j];
                arr2[j] = temp;
                Arrays.sort(arr2);
            }
        }
        
        i=0;
        for(int el : arr1) {
            temp_arr[i++] = el;
        }

        for(int el: arr2) {
            temp_arr[i++] = el;
        }

        return temp_arr;

    }


    public static void main(String[] args) {
        int[] arr1 = {1,3,5,7,9};
        int[] arr2 = {2,4,6,8,10};

        arr1 = mergeArrays(arr1, arr2);

        for (int el : arr1) {
            System.out.print(el);
        }

    }
}