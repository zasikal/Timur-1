import math
#1
a = 15
print(math.radians(a))
#2
h = 5
B1 = 5
B2 = 6
print((B1+B2)/2*h)
#3
S = int(input("number of sides:"))
L = int(input("length of the side:"))
ap = L/(2*math.tan(math.pi/S))
area = int(S*L*ap/2)
print("Area: ", area)
#4
B = float(input("Length of base:"))
h = float(input("Height:"))
print(B*h)