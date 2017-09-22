#Taking the dictionary range from the user
print("Enter the desired range for square dictionary:")
seriesrange = int(input())
#Initializing the dictionary
dictionary = dict()
#Iterating through the dictionary and appending square for the value
for number in range(1,seriesrange+1):
    dictionary[number]=number*number
#Printing the dictionary output
print(dictionary)