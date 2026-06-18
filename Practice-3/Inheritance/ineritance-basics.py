# Python Inheritance

#Create a Parent Class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a Child Class

class Student(Person):
  pass

# Now the Student class has the same properties and methods as the Person class.
x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() Function

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
