public class Shifting {

    //  algorithm used : sliding window algorithm (using swapping)
    public static void shiftTarget(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while(left <= right) {

            while(arr[right] == target) right-=1;

            if(arr[left] == target) {   //  if this true then we perform swapping
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                right-=1;
            }

            left+=1;

        }

    }

    //  insertion sorting technique
    public static void shiftUsingInsertion(int[] arr, int target) {
        int temp, j, i = 0;

        while(i<arr.length){
            temp = arr[i];
            
            if(arr[i] == target) {
                for(j = i;j<arr.length-1;j++) {
                    arr[j] = arr[j+1];
                }
                arr[j] = temp;
            }else{
                i++;
            }
        }
    }


    public static void main(String[] args) {
        int[] arr = {1,10,3,4,5,2,2,5,6,7,8,9,2,2};
        shiftUsingInsertion(arr,2);
        for(int x : arr) 
            System.out.print(x + " : ");
    }
}
