string = "everyday"
for counter in range(0, len(string)):
    for counter2 in range(0, len(string)):
        if (string[counter] == string[counter2]):
            print(string[counter], string[counter2], " Duplicate")
        else:
            print(string[counter], string[counter2], " No Duplicate")

