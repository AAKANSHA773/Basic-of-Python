a = 'Shourya'
if a == 'Apoorva':
    print('Hello Apoorva')
else:
    print("hello Shourya")

#if else with AND operator
Name = 'Tom'
password = '123'
if Name == 'Tom' and password == '123':
    print('Access Granted')

#if else with OR operator
code = 123
if code == 123 or code == 456:
    print('Access Granted')


#if condition with more then one else condition
name = 'Munnalal'
if name == 'Tom':
    print('Hello Tom')
elif name == 'John':
    print('Hello John')
elif name == 'Eric':
    print('Hello Eric')
else:
    print(' You are not allowed')


#if -elif with user input
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = input('Operator: ')
if c=='+':
    print(a+b)
elif c=='-':
   print(a-b)
elif c =='*':
    print(a*b)
else: print ('Incorrect operator')
