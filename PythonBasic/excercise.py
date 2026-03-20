#**********************************************

greeting = "Welcome to Python Programming"

print(greeting)
print(greeting + ", Deepti!")

age = 25
height = 5.9
favorite_color = "blue"

print ("Age: {}".format(age) + " | Type: {}".format(type(age)))
print ("Height: {}".format(height) + " | Type: {}".format(type(height)))
print ("favorite_color: "+ favorite_color +" | Type: {}".format(type(favorite_color)))

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit :"+fruits[0])
print("Last Fruit :"+fruits[-1])
print("Fruits from index 1 to 2: {}".format( fruits[1:3]))

person = ("Rahul",25,5.9)
print ("Age:{}".format(person[1]))

#******************************************************
dict = {"make": "Toyota","model": "Camry","year": 2020,"color": "Blue"}

print("Car model: {}".format(dict["model"]))
dict["owner"]="Rahul"
print("Updated car dictionary: {}".format(dict))


#******************************************************
user = int(input("Please enter the time in 24 hour format : "))
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")

#******************************************************
greeting =input("Enter a greeting ")
if greeting.lower() == "hello":
    print("Hello there!")
else:
    print("Greetings!")

#******************************************************

lst=[1,4,7,10]
for i in lst:
    print(i*3)