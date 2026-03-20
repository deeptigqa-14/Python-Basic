value=[1,2,3,4]
value2=[1, "Deepti", 5, True]
print (value, value[0], value[-1], value[1:3])

# value[-1] last value in the list
#  VALUE[1:3] 1 to 2 index values 2,3
print (value2)
print(value2[0], value2[1], value2[2], value2[3])
# for list item we can print the value with index number even if the data type is different

value2.append("end value")
print(value2)
value2[1] = "DEEPTI" # we can update the value in the list with index number
print(value2)
value2.insert(2, "Gupta") # we can insert the value in the list with index number
print(value2)
value2.remove("Gupta")
print(value2)
value2.insert(2, "Gupta") # we can insert the value in the list with index number
print(value2)
del value2[2] # we can delete the value in the list with index number
print(value2)