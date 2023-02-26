class Person:
  name = "Name"
  def __init__(self,name):
    self.name = name

class Student(Person):
  grade = 0

class Teacher(Person):
  salary = 0
  