"""Write a menu based program to add, peek, delete and display the record of LIBRARY using list as
stack data structure in python. Record of LIBRARY contains the information Book ID, Book type
and Book cost."""


def add(book):
    stack.append(book)


def delete():
    if not stack:
        print("Stack is empty")
    else:
        stack.pop()


def peek():
    if not stack:
        print("Stack is empty")
    else:
        stack1 = stack.copy()
        print(stack1.pop())


def display():
    if not stack:
        print("Stack is empty")
    else:
        for i in stack:
            print(*i, sep=", ")


x = int(input("Choose one of the below option numbers: \n 1) Add \n 2) Delete \n 3) Peek \n 4) Display"))
stack = [[121, "Adventure", 456], [1770, "Comic", 99]]
if x==1:
    add([789, "Drama", 121314])
elif x==2:
    delete()
elif x==3:  
    peek()
elif x==4:
    display()
else:
    print("Error in choosing option")
