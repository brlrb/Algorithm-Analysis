# Given a String, check if the string is a Permutation of a Palindrome
# Eg: 
# Input: 'tact coa'
# Output: True (Permutaiton: 'taco cat', 'atco cta', etcs)

# Useful definations
# Permutation: A string with equal length that has the same characters.
# Palindrome: A Palindrome is a word or a phrase that is the same forwards and backwards

# Algorithm Analysis
# O(n) 

# Define a function that takes string as a parameter
def palindromePermutation(string):

    # Calculate the length of a string
    stringLength = len(string)

    # Iterate through the string to check if the string can be read backwards and forwards
    for counter in range(0, stringLength):
        # If the string matches, continue and check another string
        if(string[(stringLength-1) - counter]  == string[counter]):
            continue
        else:
            # If there is a mismatch, return False
            return False
    # If all the string matches after completion of a loop cycle, return True
    return True

# Input user to enter a String
string = input("Enter a String: ")

# Call the function palindromePermutation and print the result
print(palindromePermutation(string))




