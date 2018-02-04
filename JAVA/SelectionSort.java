//Selection Sort
// https://github.com/brlrb

// STEPS:
// 1: Find the smallest unsorted element in the list and add it to the end of the sorted list
// 2: Repeat until no unsorted elements remain

// ANALYSIS
// Worst case: O(n^2)
// Best case: O(n^2)

public class SelectionSort {
    public static void main(String args[]){
        System.out.println("Selection Sort \n");

        // Variable Declaration
        int i; // counter for outer loop
        int j; // counter for inner loop
        int k; // counter for unsorted list
        int minValue; // assign the single minimun value
        int minIndex; // assign the single value of the minimum index
        int temp; // varible to hold temporary value

        // list of random values
        int[] list = {
                10, 79, 54, 41, 8, 76, 22, 5, 39, 4, 83, 99, 45, 82, 25, 100, 57, 70, 58, 89, 42, 32, 98, 47, 53, 61, 96, 56, 36, 16, 46, 92, 75, 81, 49, 29, 80, 95, 20, 44, 78, 55, 88, 26, 50, 63, 28, 71, 52, 66, 60, 12, 68, 93, 30, 73, 24, 86, 91, 34, 14, 62, 13, 38, 9, 97, 2, 64, 15, 84, 31, 3, 69, 85, 65, 77, 74, 11, 23, 67, 40, 37, 6, 94, 87, 90, 17, 7, 43, 48, 19, 21, 33, 35, 72, 27, 1, 59, 18, 51
                   };

        System.out.println("Unsorted List \n");
        for(k = 0; k < list.length; k++){
            System.out.print(list[k]+" \n");
        }


        System.out.println("Total length of the list: " + list.length + "\n");

        System.out.println("Sorted List \n");
        for ( i = 0; i < list.length; i++){
            minValue = list[i];
            minIndex = i;

            for ( j = i+1; j < list.length; j++) {
                if (list[j] < minValue){
                    minValue = list[j];
                    minIndex = j;
                };
            }

            if (minValue < list[i]) {
                temp = list[i];
                list[i] = list[minIndex];
                list[minIndex] = temp;
            }

            System.out.println(minValue);
        }
        System.out.println("\nANALYSIS");
        System.out.println("Worst Case: O(n^2)");
        System.out.println("Best Case: O(n^2) \n");
    }
}