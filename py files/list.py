l = []
l1 = []
l2 = []

def menu():
    print("\n///MENU///")
    print("1. Even & Odd")
    print("2. Merge & Sort")
    print("3. Update & Delete")
    print("4. Min & Max")
    print("5. Add names into list")
    print("6. Exit")
    return (int(input("\nEnter your choice: ")))

def evenodd():
    for i in l:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    print("\nEven nos. are: ")
    print(l1)
    print("\nOdd nos. are: ")
    print(l2)

def merge():
    l3 = l1 + l2
    print("\nThe merged list is:-\n", l3)
    l3.sort()
    print("\nSorting in ascending order:-\n", l3)
    print("\nSorting in descending order:-\n", l3[::-1])

def update():
    x = int(input("\nEnter the element to be placed in first position: "))
    l[0] = x
    print("\nThe updated list is:-\n", l)

    l.pop(n//2)
    print("\nAfter deleting middle elemtent the list is:-\n", l)        

def minmax():
    print("\nThe minimum element of list is: ", min(l))
    print("\nThe maximum element of list is: ", max(l))

def add():
    n1 = int(input("\nEnter the no. of strings to store in list: "))
    print("\nEnter the strings: ")
    for i in range(0,n1):
        s = input()
        l.append(s)
    print("\nThe updated list is:-\n", l)
    if 'python' in l:
        print("\nThe string 'python' is present in list")
    else:
        print("\nThe string 'python' is not present in list")

            
n = int(input("\nEnter the no. of elements to store in list: "))
print("\nEnter the list numbers: ") 
l = [int(x) for x in input().split()]
print("\nThe list is:-\n", l)

c=0
while(c!=6):
    c=menu()
    if c==1:
        evenodd()
    elif c==2:
        merge()
    elif c==3:
        update()
    elif c==4:
        minmax()
    elif c==5:
        add()
    elif c!=6:
        print("\nIncorrect choice")