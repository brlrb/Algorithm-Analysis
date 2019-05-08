// Merge Sort
// https://github.com/brlrb

// ANALYSIS
// Algorithm Method: Divide and Conquer
// Worst case performance: O(nlogn)
// Best case performance: O(n log n) most cases, O(n) natural variant


public class MergeSort {
    public static void main(String args[]){
        System.out.println("Merge Sort \n");

        // Variable Declaration
        int i= 0; // counter for the loop
        int k =0; // counter for the list
        boolean dataFound = false; // set data not fould

        // list of random values
        int[] list = {
                10, 79, 54, 41, 8, 76, 22, 5, 39, 4, 83, 99, 45, 82, 25, 100, 57, 70, 58, 89, 42, 32, 98, 47, 53, 61, 96, 56, 36, 16, 46, 92, 75, 81, 49, 29, 80, 95, 20, 44, 78, 55, 88, 26, 50, 63, 28, 71, 52, 66, 60, 12, 68, 93, 30, 73, 24, 86, 91, 34, 14, 62, 13, 38, 9, 97, 2, 64, 15, 84, 31, 3, 69, 85, 65, 77, 74, 11, 23, 67, 40, 37, 6, 94, 87, 90, 17, 7, 43, 48, 19, 21, 33, 35, 72, 27, 1, 59, 18, 51
        };

        System.out.println("The List \n");
        for(int l:list) {
            System.out.print(l+" ");
        }
        System.out.println("\n\nTotal length of the list: " + list.length + "\n");





        while (i > list.length){

            System.out.println("\n\nThe list: " + i + "\n");

        }



        System.out.println("\nANALYSIS");
        System.out.println("Worst Case Performance: O(nlogn)");
        System.out.println("Best case performance: O(nlogn) - most cases, O(n) natural variant \n");
    }
}