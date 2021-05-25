list1=[10,20,"aaku",-10,49,5.1]
#Many way of print list
print(list1)
print(list1[3])
print(list1[3:5])
print(list1*4)

#some inbuild function of list
# length of list
print(len(list1))

#append value in the list
list1.append(56)

#delete elements in the list 
del(list1[2])
print(list1)

#find max value in the list
print(max(list1))

#find min value in the list
print(min(list1))

#insert value in the list.
list1.insert(4,100)
print(list1)

#sort value in increasing and decreasing order
list1.sort(reverse=True)
print(list1) 

#remove value in the list
list1.remove(-10)
print(list1)

#clear list
list1.clear()
print(list1)

#join to two list
lst2=[3,5,7,8]
lst3=["akku","nidhi","ranju"]
lst4=lst2+lst3
print(lst4)

fruits = ["mac","eddy","ela","roy","eddy"]
x = fruits.count("eddy")
print(x)
