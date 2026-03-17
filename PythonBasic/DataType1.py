# Here is my 1st Python program

print('welcome')
a , b, c = 5, 10.1, "Deepti"

print("{} {} {}".format("Value is ",a, b))

print(type(a))
# {} used to concatnate 2 different data types
age, height, favorite_color = 25, 5.9, 'blue'
print ("{} {} {} {}".format("Age: ", age, "| Type: ", type(age)))
print (f"Age: {age} | Type: {type(age)}")

print("Age: {} | Type: {}".format(age, type(age)))

# List data type starts with 0 index
list_values =[1,2.1,"Deepti", True]
print(list_values[3])
print(list_values[-1]) # -1 index gives last value
print(list_values[1:3]) # 1 to 2 index values
print(list_values[1:]) # 1 to last index values
print(list_values[:3]) # 0 to 2 index values
print(list_values[:]) # all values

list_values.insert(3,'Gupta')

list_values.append('New Value')
list_values[4] = False
del list_values[5]
print (list_values)

