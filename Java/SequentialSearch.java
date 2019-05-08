//Sequential Search or Linear Search
// https://github.com/brlrb

// ANALYSIS
// Algorithm Method: Brute Force
// Worst case performance: O(n)
// Best case performance: O(1) - If the item we are searching is the first item


import java.util.Scanner;  // import Scanner

public class SequentialSearch {
    public static void main(String args[]){
        System.out.println("Sequential Search \n");

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

        Scanner scanner = new Scanner( System.in );

        System.out.println("Enter a number to search: ");
        int userInput = scanner.nextInt();
        System.out.print("You entered: " + userInput + "\n");


        while (i < list.length && !dataFound){
            if (userInput == list[i]) {
                System.out.println(userInput + " found! " + " at index " + i);
                dataFound = true; // set counter to the end of the list and exit as soon as we find a match
            } else {
                i++;
            }
        }
        if (dataFound == false) {
            System.out.println(userInput + " not found");

        }


        System.out.println("\nANALYSIS");
        System.out.println("Worst Case Performance: O(n)");
        System.out.println("Best case performance: O(1) - If the item we are searching is the first item \n");
    }
}