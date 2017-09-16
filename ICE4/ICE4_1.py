#Defining the class
class student(object):

    student_count = 0
#Defining the constructor
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
        student.student_count += 1

#Calculating the number of students using their object variable
    def getstudentscount(self):
        print('The number of students are', student.student_count)

# Function to get Student name, roll no and grades
    def getstudentdetails(self):
        print("The student details are: ", "Name - " , self.name, ",", "ID -" , self.id ,",","Grades -" , self.grade)

#Function to add a student
  #  def addStudent(self, name, id, grade):
       # self.name = name
        #self.ID = id
        #self.Grade = grade
        #addstudent = student(name, id, grade)
        #print("The student was added")

class TransferStudent(student):
    def __init__(self, name, id, grades, university):
        student.__init__(self, name, id, grades)
        self.university=university
    def getstudentdetails(self):
        student.getstudentdetails(self)
        print("Transferred from university :",self.university)


"""print("Enter the student's name, ID, grade to add")
Name = str(input())
idnum = int(input())
Grade = str(input())"""
#Creating list for Student instances with attributes
StudentList = []
StudentList.append(student("Vamshi", 1279, ['A','A','B']))
StudentList.append(student("Shivam", 2899, ['A','A','B']))
StudentList.append(TransferStudent("Swapna", 1326, ['A','A','B'],"UCD"))
StudentList.append(TransferStudent("Satish", 2613, ['A','A','B'],"IITC"))

#Iterating through student list to display details
for object, item in enumerate(StudentList):
    item.getstudentdetails()
    print("\n")
    if object == len(StudentList)-1:
        item.getstudentscount()

