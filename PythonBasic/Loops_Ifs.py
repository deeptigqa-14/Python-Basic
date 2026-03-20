greeting = "Good morning"
if greeting =="Good morning":
    print("The greeting is correct")
else:
    print("The greeting is incorrect") # it is case sensitive

    newString = "test string"
    print(newString) # will not print as it is in else block
# indentation is important in python

#for loop
list_obj= [1,9,3,4,6,2]
print("length of the list is : {}".format(len(list_obj)))

print(f"length of the list is : {len(list_obj)}")
for i in list_obj:
    print(i)
# sum of five natural numbers

sum =0
for j in range(6): # 1 to 5 range (i, j) --> i to j-1
    sum = sum + j
   # print(j)

print(f"Total is : {sum}")
print("Total is : {}".format(sum))


for j in range(10,1,-2): # 1 to 10 with step 5 ans 1, 9
    sum = sum + j
    print("Jump number : {}".format(j))

#while loop
it = 10
print ("While loop starts")
while it >=1 :
    if it==7:
        it = it-1
        continue # will skip the value 7 and continue the loop (whole while loop
    if it == 3:
        print("It is 3, breaking the loop")
        break # will break the loop when it is 3 , it will be out of while as well
    print(it)
    it = it-1

