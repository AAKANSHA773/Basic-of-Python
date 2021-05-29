d2=dict()
print("empty dictionary",d2)

d1={}
print("empty dictionary repersant",d1)

d={'1':"one"}
print("key and value",d)

d3={'1':"one",'2':"two",'3':"third",'4':"string"}
print(d3)

d3['1']='100'#chnage the value of index one element
print(d3)

d3[1]=[1,2,3] #give value in the from of list
print(d3)

print("two" in d3.values()) # check value are present or not in this dictinary

#dict = key: values

dict1={1:"akku",2:"ammu",3:"aadi"}
print(dict1)

print(dict1.items()) #print key value in the form of set

k=dict1.keys()#  for print keys
for i in k:
    print(i)

v=dict1.values() # print values
for i in v:
    print(i)

print(dict1[1]) # dictionary index start with 1.

del dict1[2] # delete specific index key-value 
print(dict1)
