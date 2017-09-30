# Adds string to the list
wordList = []
stringNumber = input("Enter the number of strings: ")
print("Enter the strings")
#Looping through string inputs
for i in range(0,int(stringNumber)):
    string = input()
    wordList.append(string)
#List to populate the string lengths
lengthList=[]
for word in wordList:
    lengthList.append(str(len(word))+  "," + word)
lengthList.sort()
#Print the strings and lengths
print(lengthList)

#Finding the maximum length string
longestLength = max(len(word) for word in wordList)
print(longestLength)


