# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []

def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result


friend(["Ryan", "Kieran", "Jason", "Yous"])