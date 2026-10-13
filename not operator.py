a=10
b=12
c=12

print(not(a==b))

print(not(b==c))

a="Hello World"
b="shaurya"

if not(a==b):
    print(a,"and",b,"are different")

a=int(input("Enter a number:"))
if not(a%2==0):
    print(a,"is a odd number")
else:
    print(a,"is a even number")