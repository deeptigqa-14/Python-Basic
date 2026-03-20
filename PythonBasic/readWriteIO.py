# reading
file = open("test.txt")
#print(file.read(20)) # read first 20 characters
file.close()

file = open("test.txt")
# print("Read with loop")
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

#for line in file.readlines():
 #   print(line)

for line in file.readlines():
    print(line)

file.close()

#writing
with open("test.txt", "r") as reader:
    content = reader.readlines() # store the content of the file in a list
    sorted(content)
    print(content)
    reversed(content)
    print(content)
with open('writetest.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)
    writer.write("This is new line at the end of the file")
    