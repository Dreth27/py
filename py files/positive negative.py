a = int(input("\nEnter the first number: "))
b = int(input("\nEnter the second number: "))

print('\nBefore swap:-')
print('a = ', a, '\nb = ', b)

temp = a
a = b
b = temp

print('\nAfter swap:-')
print('a = ', a, '\nb = ', b)

if a>0:
	print('\nThe no. ', a, ' is positive')
elif a<0:
	print('\nThe no. ', a, ' is negative')
else:
        print('\nThe no. is zero')
