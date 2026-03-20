
# Declare function to print my name
def greetme(name):
    print("Welcome " + name)
# call the function
def addon(a, b):
    print (f"Sum is : {a+b}")
    return a+b
# function to greet user
def greetuser(name):
    print("Hello," + name+"! Welcome to Python programming.")

greetme("Deepti")
print (addon(5, 10))

name= input("Enter your name : ")
greetuser(name)

