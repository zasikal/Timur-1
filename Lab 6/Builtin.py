#1
from functools import reduce 
from operator import mul
mylist = [1, 2, 3, 4, 5]
print (reduce(mul, mylist))
#2
mystr = "ABpopa HukoLb"
upp = 0
low = 0
for x in mystr:
    if x.isupper() == True:
        upp = upp + 1
    if x.islower() == True:
        low = low + 1
print ("There are " + str(upp) + " uppcase letters and " + str(low) + " lowcase letter")
#3
mystr1 = "AbobA"
mystr2 = "ABarua"
if mystr1 == mystr1[::-1]:
   print(mystr1 + " is a palindrome")
else:
   print(mystr1 + " is not a palindrome")
if mystr2 == mystr2[::-1]:
   print(mystr2 + " is a palindrome")
else:
   print(mystr2 + " is not a palindrome")
#4
import time
import math
a = 25100
b = 2123
time.sleep(b/1000)
print("Square root of " + str(a) + " after " + str(b) + " milliseconds is " + str(math.sqrt(a)))
#5
mytuple1 = (True, True, 1 ,True)
mytuple2 = (True, False, 2 ,True)
print(all(mytuple1))
print(all(mytuple2))