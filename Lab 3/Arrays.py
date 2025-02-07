#Access to array
arr = ["Ford", "Volvo", "BMW"]
x = arr[0]
print(x) #Ford
arr[0]="Toyota"
x = arr[0]
print(x, '\n') #Toyota

#Length
car = ["Ford", "Volvo", "BMW"]
x = len(car)
print (x) #3

#Looping through
for x in car:
    print(x) #Ford Volvo BMW

#Adding element
car.append("Honda") #added Honda to the end
print (car)

#Removing elements
car.pop(1) #Remove 2nd element Volvo
print (car)

car.remove ("Ford") #Remove Ford
print (car)