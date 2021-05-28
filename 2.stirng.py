s="you are awesome"
print(s)

print(s[2])#print index 2 value, it also count space
print(s*2)

#string slicing - start,stop, step,
print(s[0:6])#step by defult 1
print(s[5])
print(s[:8])
print(s[-1]) #print last element of string
print(s[-4:-1])

s1=""" You are the creator of your destiny  """
print(s1)

print(len(s1))
print(s1[0:9:2])
print(s1[::-1]) #reverse of string



#strip =strip use for remove space 
print(s1.strip())#remove both left and right space
print(s1.lstrip())#remove left space
print(s1.rstrip())#remove right space

print(s1.find("are"))# give starting index of this string

print(s.count("a")) # give index number of first a.

print(s.split("e")) # it give break if "e" is count.

a="Hello"
b="Everyone"
c="I am aakansha"
print(a +" "+ b + " "+ c )#string concatination

print(s.replace("awesome","super"))

print(s.upper())

print(s.lower())

print(s.title())
