# reading
file = open("test.txt")
#content =(file.read(10)) #will print first 10 characters including lines , space is treated as character

#Line1 = file.readline() # will print 1st line
#Line2 = file.readline() # will print 2nd line

#line = file.readline()
#while line !="":
 #   print(line)
 #   line = file.readline()

#for line in file.readlines():
 #   print(line)

file.close()

# writing
with open("test.txt", "r") as reader:
    content = reader.readlines()
   # reversed(content)
with open('test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)