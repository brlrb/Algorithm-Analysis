# Given two strings, write a method to decide if one is a permutation of the other.
# Permutation: A string with equal length that has the same characters.


# Rules:
# 1: The input letter(s) are case sensitive. So 'A' is not same as 'a'
# 2: The input letter(s) white spaces matters. So 'A ' is not the same as 'A' 


def isPermutation(string1, string2):
    if(len(string1) != len(string2)):
        return False


    if(sorted(string1) == sorted(string2)):
        print("sorted", sorted(string1), sorted(string2))
        return True

    return False


# Prompt user to enter a String1
string1 = input("Enter string one: ")

# Prompt user to enter a String2
string2 = input("Enter string two: ")

# Call the function isPermutation and print the result
print(isPermutation(string1, string2))