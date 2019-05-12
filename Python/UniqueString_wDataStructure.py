# Implement an algorithm to determine if a string has all unique characters. 


# Using `set` data structure O(1)
def is_unique_string(string):
    # `set` removes duplicate characters because The elements in the set cannot be duplicates.
    if len(string) > 128:
        return False
    return len(string) == len(set(string))


# Prompt user to enter a String
string = input("Enter a String to check if it has unique characters: ")

# Call the function is_unique_string and print the result
print(is_unique_string(string))