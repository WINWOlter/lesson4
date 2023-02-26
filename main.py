class Person:
  name = "Name"
  def __init__(self,name):
    self.name = name

class Student(Person):
  grade = 0
  def study(self):
    self.grade += 1

  def __init__(self):
    super().__init__("Student")

class Teacher(Person):
  salary = 0
  student = []

  def study(self):
    self.salary += 1000
  
  def __init__(self):
    super().__init__("Teacher")
    
  def set_grade(self,student):
     student.grade = 12

teacher = Teacher()
print(teacher.salary)

student = Student()

print("оцінка до",student.grade)
teacher.set_grade(student)
print("оцінка після",student.grade)
    



print(student.grade)

student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()
student.study()


print(student.grade)


  