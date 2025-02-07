#Lambda - a small function
#Example
x = lambda a : a + 10
print(x(5), '\n') #15
x = lambda a, b: a*b
print(x(5, 6)) #30
x = lambda a, b, c: a + b * c
print(x(5, 2, 4), '\n') #13
#"Helpful" usage of Lamda
def my_function(n):
    return lambda a: a*n
mydoubler = my_function(2)
print(mydoubler(11))