thislist = ["apple", "banana", "cherry", "apple", "cherry", 1, 2, True, False, 2+4]
print(thislist)
print(len(thislist))

list1 = list(("abc", 34, True, 40, "male"))
print(list1)
print(type(list1))
print(list1[1], list1[-1])
print(list1[1:3])
print(list1[2:], '\n')
print(list1[:4])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "40t0"
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)
thislist.append("Arbyz")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.remove("apple")
print(thislist)
thislist.pop(1)
print(thislist)
#just listname.pop() removes the last item
#listname.pop(0) = del listname[0]
#del listname - deletes full list
print('\n')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist, '\n')

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print('\n')

for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

print('\n', "SOOOOORTIROOOOVKA", '\n')
#by alphabet and Size
thislist = ["Orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#descending
thislist.sort(reverse = True)
print(thislist)
#howcloseto
def myfunc(n):
  return abs(n - 50)

thislist.sort(key = myfunc)
print(thislist)
#insensitive list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


print('\n' "COOOOOPYIIIING", '\n')

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

print('\n' "JOOOOOOINIIIIING", '\n')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)