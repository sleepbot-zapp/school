"""Create a dictionary containing names and marks as key value pairs of 6 students. Write a program, with separate user defined functions to perform the following operations:
a. Push the keys (name of the student) of the dictionary into a stack, where the corresponding value (marks) is greater than 75.
b. Pop
c. Display the content of the stack"""


students = {"Prithi":40, "Sounak":50, "Shubham":60, "Shahanur":70, "Reshma":80, "Jyoti":90}
stack = {}


def push():
    for i, j in students.items():
        if j>75:
            stack[i] = j


def pop():
    stack.pop(list(stack.keys())[-1])


def display():
    for i, j in stack.items():
        print(f"{i} : {j}")

push()
pop()
display()
