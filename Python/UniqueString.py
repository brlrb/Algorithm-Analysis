# Implement an algorithm to determine if a string has all unique characters. 


# 1: Using `set` data structure O(1)
def is_unique_string(string):
    # `set` removes duplicate characters because The elements in the set cannot be duplicates.
    if len(string) > 128:
        return False
    return len(string) == len(set(string))


# 2: Using `count` data structure - O(n)
def is_unique_string_count(string):
    # `set` removes duplicate characters because The elements in the set cannot be duplicates.
    if len(string) > 128:
        return False

    return False if (string.count(string[counter]) > 1) for counter in range(0, len(string)) else return True



# 3: What if you cannot use additional data structures? O(n^2)
def is_unique_string_clean(string):
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
                    print("uniqueCount", uniqueCount)
                    return False
                
            
    # return True if all characters are unique
    return True




# start the program
def init():
    print("* Implement an algorithm to determine if a string has all unique characters *")
    print("1: Using a Data Structure")
    print("2: Using a `Count` Data Structure")
    print("3: Without using a Data Structure")
    print("0: Exit the program")
    val = input("Select the type of algorithm you want to use? (1 or 2. 0 to Exit.) ")
    algo_select = int(val)


    # Users selection
    if(algo_select == 1):
        print("... using a Data Structure.")
        string = input("Enter a string to determine if a String has all Unique Characters: ")
        print(is_unique_string(string))

    elif(algo_select == 2):
        print("... Using a `count` Data Structure.")
        string = input("Enter a string to determine if a String has all Unique Characters: ")
        print(is_unique_string_count(string))
    
    elif(algo_select == 3):
        print("... Not using a Data Structure.")
        string = input("Enter a string to determine if a String has all Unique Characters: ")
        print(is_unique_string_clean(string))

    elif(algo_select == 0):
        print("Goodbye")

    else:
        print("Invalid selection, run the program again")
        init()


# Initialize the program 
init()
