
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
# Calculate average of 3numbers
def avg(a, b, c):
    return (a+b+c)/3


greetme("Deepti")
print (addon(5, 10))

name= input("Enter your name : ")
greetuser(name)

a= int(input("Enter a number1 : "))
b=int(input("Enter a number2 : "))
c=float(input("Enter a number3 : "))
print(f"The average of {a},{b}, and {c} is {avg(a, b, c)}")


with open("test.txt","r") as f:
    print(f.read())
    # while True:
    #     line = f.readline()
    #     print(line)
    #     if not line:
    #         break
