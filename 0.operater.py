#print function
print()
name="akku"
markes=55.353

print("name is %s, marks are %.3f"%(name, markes))
print("name is ", name,"marks is",markes)

print("anme is {}, markes are {}".format(name,markes))
print("anme is {0}, markes are {1}".format(name,markes))

# variable.assignment 
a=b=c=10
print(a,b,c)

x,y=10,5
x+=y
print(x)

x*=y
print(x)

# arthmetic operation 
a,b=10,5

print("addition",a+b) 
print("subtraction",a-b)
print("multiply",a*b)
print("devision",a/b)
print("mod",a%b)
print("pow",a**b)
print("floor div",a//b)

#comparision operater
x,y=77,88
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

#logical operator
x=10
y=30
print(x==10 and y==30)
print(x==10 or y==10)
print(x==23 and y==30)
print(x==24 or y==30)
print(not(x==24 or y==43))
print(not(x==10 or y==30))

#user input function
s=input("enter your name :")
print(s)

i= int(input("enter a integer number"))
print(type(i))

lst= [x for x in input("enter three number seprated by space:").split()]
print(lst)
