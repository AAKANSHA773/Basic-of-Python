#set are unchangeable,once a set is created, we can not change its items.

s={10,20,30,39,30}#not allow duplicate
print(s)


s.update([55.77])
print(type(s))
print(s)

#not support indexing, slicing ,not perform reptation
s.remove(30)
print(s)

print(len(s)) #lenght of set
