public class Insertion {

    public static void insertionSort(int[] arr) {
        int j, temp;

        for(int i=1;i<arr.length;i++){
            temp = arr[i];
            j=i-1;
            while (j>=0 && arr[j] > temp) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {-1, 1,2, 3,-5,89,12,6,7,8,-10};
        insertionSort(arr);
        for(int x : arr) 
            System.out.println(x + " : ");
    }
}
