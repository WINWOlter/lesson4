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

student = Student()

print(student.grade)

student.study()


print(student.grade)


  