inputList = [{'Course': 'Python', 'LastGPA': 85, 'CurrentGPA': 90},
             {'Course': 'Python', 'LastGPA': 90, 'CurrentGPA': 95},
             {'Course': 'Python', 'LastGPA': 95, 'CurrentGPA': 100}]

# Function to average GPA's
def avgGPA():
    for gpa in inputList:
        avgGPA = (gpa.get('LastGPA') + gpa.get('CurrentGPA')) / 2
        gpa.pop('LastGPA')
        gpa.pop('CurrentGPA')
        gpa['Average GPA'] = int(avgGPA)
    return inputList


print("Input Dictionary List")
print(inputList, "\n")
print("Output")
print(avgGPA())