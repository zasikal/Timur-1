#Creating a class
class MyClass:
    x=5
print (MyClass) #class of Myclass
#Creating an object
p1 = MyClass()
print(p1.x) #5

#__init__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) #John
print(p1.age) #36

#__str__() function
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
      return f"{self.name}({self.age})"
p1 = Person("John", 36) #John(36)
print(p1)

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   def __str__(self):
      return f"Hello, my name is {self.name} and i'm " + str(self.age) + f" years old"
p1 = Person("John", 36)
print (p1) #Hello, my name is John and i'm 36 years old

#Self parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() #Hello my name is John

#Modifying 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p1.age = 40
print(p1.age) 