#Hardcoded string
inputstring = "This is an example to sort words using a list"

# uncomment to take input from the user
#inputstring = input("Enter a string: ")

# breakdown the string into a list of words
words = inputstring.lower().split()

# Using sort() method to sort the list alphabetically
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)