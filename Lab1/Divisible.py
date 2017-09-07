#List to display resultant numbers
resultlist=[]

#Looping through numbers between 700 and 1700
for number in range(700, 1700):

    #Condition for divisible by 5 and multiple of 2
    if (number%5==0) and (number%2==0):
        resultlist.append(str(number))
print ("The numbers divisible by 5 and multiples of 2 are :" + "\n" + str(resultlist))