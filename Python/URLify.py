# Write a program to replace all the spaces in a string with %20. 
# You may assume that a given string has sufficient space at the end to hold the additional characters.

# Define the function urlify
def urlify(string):
    # Convert the string into a list because String in Python is Immurable(it cannot be changed)
    stringList = list(string)
    # Iterate through each index of the string and check if there are space.
    for counter in range (0, len(string)):
        # If the index matches a space, replace the index with '%20'
        if(stringList[counter] ==' '):
            stringList[counter] = '%20'
    
    # Upto this point the string is in list format. We can convert list into String by using `''.join(...list...)` 
    string = ''.join(stringList)
    
    # return back the string value
    return string


# Prompt user to enter a String
string = input("Enter a String: ")

# Call the function urlify and print the result
print(urlify(string))