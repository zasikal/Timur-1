#1
def squares(N):
    a = 1
    while a < N:
        yield a*a
        a += 1
N = int(input())
for kvadrat in squares(N):
    print(kvadrat)
#2
def evenN(n):
    a = 0
    while a < n+1:
        if (a%2==0):
            yield a
        a += 1
n = int(input())
print(", ".join(str(b) for b in evenN(n)))
#3
def div34(n):
    a = 0
    while a < n+1:
        if(a%12==0):
            yield a
        a +=1
n=int(input())
for b in div34(n):
    print(b)
#4
def squares(a, b):
    while a<b+1:
        yield a*a
        a += 1
a=int(input("input starting number:"))
b=int(input("input ending number:"))
for c in squares(a,b):
 print(c)
#5
def naoborot(n):
    while n>-1:
        yield n
        n -=1
n=int(input())
for b in naoborot(n):
    print(b)