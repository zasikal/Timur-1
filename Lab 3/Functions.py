#Creating and calling a function
def my_function():
    print("Hello, World!", '\n')
my_function()
#Hello, World!

#Arguments
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil") #Emil Refsnes
my_function("Tobias") #Tobias Refsnes
my_function("Linus") #Linus Refsnes 
print('\n')

#Also arguments
def my_function(fname, lname):
    print(lname + " " + fname, '\n')
my_function("Emil", "Refsnes") #Refsnes Emil

#Arbitrary arguments (*args)
def my_function(*kids):
    print("The youngest child is - " + kids[2], '\n') #[0,1,2]
my_function("Emil", "Tobias", "Katya") #...Katya 

#Keyword
def my_function(child1, child2, child3): #doesn't work with *args
    print("The youngest child is - " + child2, '\n') #...Tobias
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Katya")

#But works with **kwargs 
def my_function(**kids): #doesn't work with *args
    print("The youngest child is - " + kids["child1"], '\n') #...Emil
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Katya")

#Passing a list
def my_finction(Fruits):
    for x in Fruits:
        print(x)

Fruits = ["apple", "banana", "cherry"]
my_finction(Fruits)
#apple banana cherry
print('\n')

#Returning values
def my_function(x):
    return x * 3
print(my_function(3))#9
print(my_function(5))#15
print('\n')

#Positional only arguments (idk what it does)
def my_function(x, /):
  print(x, '\n')

my_function(3)#3

#Keyword only arguments (whats the purpose of this??)
def my_function(*, x):
  print(x, '\n')

my_function(x = 3) #3

#Example
def my_function(a, b, /, *, c, d):
  print(a + b + c + d, '\n')

my_function(5, 6, c = 7, d = 8)
#26 

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)