// Insertion Sort
// https://github.com/brlrb

// ANALYSIS
// Algorithm Method: Decrease and Conquer
// Worst case performance: O(n^2)
// Best case performance: O(n)


public class InsertionSort {
    public static void main(String args[]){
        System.out.println("Insertion Sort \n");

        // list of random values
        int[] list = {
                10, 79, 54, 41, 8, 76, 22, 5, 39, 4, 83, 99, 45, 82, 25, 100, 57, 70, 58, 89, 42, 32, 98, 47, 53, 61, 96, 56, 36, 16, 46, 92, 75, 81, 49, 29, 80, 95, 20, 44, 78, 55, 88, 26, 50, 63, 28, 71, 52, 66, 60, 12, 68, 93, 30, 73, 24, 86, 91, 34, 14, 62, 13, 38, 9, 97, 2, 64, 15, 84, 31, 3, 69, 85, 65, 77, 74, 11, 23, 67, 40, 37, 6, 94, 87, 90, 17, 7, 43, 48, 19, 21, 33, 35, 72, 27, 1, 59, 18, 51
        };

        System.out.println("The List \n");
        for(int l:list) {
            System.out.print(l+" ");
        }
        System.out.println("\n\nTotal length of the list: " + list.length + "\n");


        for (int i = 1; i < list.length ; i++) {
            int key = list[i];
            int j = i - 1;

            while ( (j > -1) && ( list[j] > key ) ) {
                list[j+1] = list[j];
                j--;
            }
            list[j+1] = key;

        }
        for(int k = 0; k < list.length; k++){
            System.out.print(list[k]+" ");
        }


        System.out.println("\nANALYSIS");
        System.out.println("Worst case performance: O(n^2)");
        System.out.println("Best case performance: O(n) \n");
    }
}