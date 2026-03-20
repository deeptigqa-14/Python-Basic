str = "rahulshettyacademy.com"
str1 = "python"
str2 = "rahul"
print(str[2]) # will print h
print (str[0:5]) #for substring 0 to 4 index it will print Rahul
print (str[0:5:2]) # 0 to 4 index with step
print("string is :"+str+" " + str1) # concatenation

print(str2 in str) # will return True if str2 is present in str
print(str2 not in str) # will return False if str2 is present in str

strsplit =  str.split(".")
print (strsplit) # will split the string at h and return list
print (strsplit[1])
str4 = " great "
print(str4.strip()) #lstrip and rstrip will remove spaces from left and right
print(str4.replace("great","good")) # will replace great with good , will work with single character also
