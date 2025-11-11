import pickle
import datetime

class student :
    def __init__(self) :
        self.name = ""
        self.registerNumber = 0
        self.DOB = datetime.datetime.now()
        self.fullTime = True

studentRecord = student()

myFile = open(r"C:\Users\aarus\Desktop\GIT\RandomCode\Learning\Student.DAT", 'w+b')

studentRecord.name = input("Enter your name: ")
studentRecord.registerNumber = input(f"Enter your register number {studentRecord.name}: ")
year = int(input("Enter you year of birth (YYYY): "))
month = int(input("Enter your month of birth (MM): "))
day = int(input("Enter your date of birth (DD): "))

studentRecord.DOB = datetime.datetime(year, month, day)
studentRecord.fullTime = bool(input("Enter True if you are full time or False otherwise :"))

pickle.dump (studentRecord, myFile)

myFile.close()

myFile = open(r'C:\Users\aarus\Desktop\GIT\RandomCode\Learning\Student.DAT','rb')
studentRecord = pickle.load(myFile)
print(studentRecord.name, studentRecord.registerNumber, studentRecord.DOB,
 studentRecord.fullTime)
myFile.close()
