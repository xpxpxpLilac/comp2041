#!/usr/bin/python3
name = input("what's your name?\n")
print("hello",end="")    #newline if no "end="""
print("\n")
print("hello",end=",")
print("\n")
print("welcome","to","New","York") #separated by spaces

x=input("Number 1:")
y=input("Number 2:")
print(x+y)                   #x,y are both string,
			     #although they are number as input
print(type(10))
print(int(10))
name = input("Enter your name: ")
year = int(input("Enter your birthyear: "))
print("Hello {1}! You are {0} years old".format(name, 2017 - year)) #0 and 1 are order of argument
print(f"Hello {name}! You are {2017-year} years old")
