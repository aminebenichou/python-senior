# Class Creation
class Student():
    name = ""
    last_name = ""
    age = 0
    moyenne = 0.0
    student_id = 0

    def displayFullName(self):
        print(self.name, self.last_name)




i=0
student_list = []
while i< 3 :
    student = Student()
    student.name = input("Enter the student's name: ")
    student.last_name = input("Enter the student's last name: ")
    student_list.append(student)
    i += 1
print(student_list)

for student in student_list:
    print(student.name)