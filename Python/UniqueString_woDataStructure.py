# Implement an algorithm to determine if a string has all unique characters. 


# Without using any data structures? O(n^2)
def is_unique_string(string):
    uniqueCount = 0
    string_len = len(string)

    for counter in range(0, string_len):
        # reset the unique counter for new iteration
        uniqueCount = 0

        for counter2 in range(0, string_len):
            if (string[counter] == string[counter2]):

                # increment the counter if there is more than one match 
                # because 1st match is obvious but second match indicates that 
                # there is more than one character and it is not unique.
                uniqueCount = uniqueCount + 1
                
                # if the uniqueCount counter is more than 2, this means there is more than one match
                # return False if uniqueCount > 1  
                if(uniqueCount > 1):
                    return False
                
            
    # return True if all characters are unique
    return True

# Prompt user to enter a String
string = input("Enter a String to check if it has unique characters: ")

# Call the function is_unique_string and print the result
print(is_unique_string(string))