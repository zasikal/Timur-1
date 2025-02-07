#Parent and child classes
#Create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()#John Doe
#Creaate a child class
class Student (Person):
  pass

y = Student("Mike", "Oisen")
y.printname()#Mike Oisen
print ('\n')



#Add init function to the child class
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname, '\n')

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname() #Mike Oisen



#Super() function
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname() #Mike Oisen

#Adding properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear) #2019

#Adding methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()