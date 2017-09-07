#input gameboard height and length
heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))
#Function to print gameboard rows
def printHorizon(widthinp):
        print(" ---" * widthinp)
#Function to print gameboard columns
def printVertical(heightinp):
        print("|   " * (heightinp + 1))
#Building matrix for Gameboard
for index in range(heightinp):
    printHorizon(widthinp)
    printVertical(heightinp)
printHorizon(widthinp)