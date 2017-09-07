#Reference string containing all alphabets
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Enter the sentence:")
phraseLetters=str(input())

#Function to check alphabets in a string
def alphabetCheck(sentence, alphabet):

#Eliminating Upper case to remove redundancy
    tempString = str.lower(sentence)
    string=str.replace(tempString,' ','')

#Looping through each letter in input strings
#Terminate and return false if not
    for alpha in alphabet:
        if str.find(string,alpha)==-1:
            return False
            break
        else:
            return True
    
#Passing input and alphabets through the function
#Return true if string contains all alphabets, false otherwise
if(alphabetCheck(phraseLetters,alphabet)==True):
    print("The string contains all alphabets")
else:
    print("The string does not contain all alphabets")
