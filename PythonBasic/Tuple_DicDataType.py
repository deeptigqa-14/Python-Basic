# tuple
# once created, cannot be modified
# can contain duplicate values immutable

tuple_values = (True,2,"Deepti",4.5)
print(tuple_values[2])
print(tuple_values[-1])
print(tuple_values[1:3]) # 1 to 2 index values
print(tuple_values[1:])
print(tuple_values[:3])

# dictionary
# key value pair
# unordered, mutable, indexed
# no duplicate keys allowed
dict_values = {"Name":"Deepti",
               "Age":25,
               "Height":5.0,
               "LName":"Gupta",
               4: "int Key"} # duplicate key not allowed, last value will be considered
print(dict_values[4]) # accessing value using key
print(dict_values["Name"])

# dynamic dictionary creation
dynamic_dic ={}
dynamic_dic["Name"] = "Deepti"
dynamic_dic["Age"] = 25
dynamic_dic["Height"] = 5.0
dynamic_dic["female"] = True
print(dynamic_dic)
dynamic_dic["NewValue"] = "New Value"
print(dynamic_dic)

