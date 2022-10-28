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


print("Choose one of the below option numbers: \n 1) Add \n 2) Delete \n 3) Peek \n 4) Display")
stack = [[121, 234, 456], [1770, 100, 99]]
add([789, 91011, 121314])
delete()
peek()
display()
