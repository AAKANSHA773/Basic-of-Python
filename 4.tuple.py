t=tuple()
print("empty tuple =",t)

tpl2=(40) #it consider as a int
print(type(tpl2))

tpl2=(40,) # now it is tpl
print(type(tpl2))

tpl=(10,20,10,30,"mee")
print(tpl)

print(tpl[2])
print(tpl*3) #print tuple in many times

print(tpl.count(10)) # count number of times 10
print(tpl.index(20)) # index of a specific position

lst=[34,56,76,32,"xyz"]
print(type(lst))
tpl1=tuple(lst) # list convert into tuple and vice versa
print(type(tpl1))

t1=(12,23,44,19)
t2=(44,)
print("concatinate",t2+t1) #concatination of tuples

print("append",t1+(30,)) #append new element in tuple

print(t1[0:]) #slicing

print("length of tuple ",len(t1)) #lenght of tuple

s1={1,2,3}
s2={2,3,4,5}
print("union in this sets",s1.union(s2)) #union of two tuples
print("intersection",s1.intersection(s2)) #intersection of two tuples
