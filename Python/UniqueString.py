# Algorithm to determine if a String has all Unique Characters

def is_unique_string(string):
    return len(string) == len(set(string))


S = input("Enter a string to determine if a String has all Unique Characters: ")


print(is_unique_string(S))
