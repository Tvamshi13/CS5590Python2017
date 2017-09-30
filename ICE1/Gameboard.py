import random
randomNumber = random.randint(0,9)
print("Please enter a number between 0 to 9")
guessNumber = int(input())
if(guessNumber>randomNumber):
    print("Your guess is greater")
elif(guessNumber==randomNumber):
    print("Perfect guess!!")
else: print("Your input is lesser")
