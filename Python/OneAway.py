# Given two strings, write a function to determine if they are one edit(or zero edit) away. 
# Three types of edits are allowed: Insert, Remove and Replace.

# Eg:
# - Pale, Ale  ->  True
# - Ball, All  ->  True
# - Soft, So   ->  False


def oneAway(string1, string2):

    if(abs(len(string1) - len(string2)) > 1):
        return False
    
    sortedString1 = sorted(string1)
    sortedString2 = sorted(string2)
    


# Prompt user to enter a String1
string1 = input("Enter string one: ")

# Prompt user to enter a String2
string2 = input("Enter string two: ")

# Call the function oneAway and print the result
print(oneAway(string1, string2))