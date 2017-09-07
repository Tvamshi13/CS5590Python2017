#Reading from the input file
openFile = open('Text.txt','r')

#Writing output to the output file
outputFile = open('Output.txt','w')

#Initialising count list
wordCount = {}
paragraph = openFile.read().lower().split()

for word in paragraph:
    if word not in wordCount:
        wordCount[word] = 1
    else:
        wordCount[word] += 1

#Writing words and their count to the file

for count,word in wordCount.items():
    str(word).replace('.','')
    outputFile.write(str(word) + "," + str(count))
    outputFile.write("\n")

print("The output file is prepared")

#Close both the files
openFile.close()
outputFile.close()

