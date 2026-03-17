items = 0

if items != 5:
    #raise Exception("Less than 5 items!")
    #raise ValueError("Invalid number of items!")
    pass

#assert(items == 5), "Items is not 5"

# try and except(catch) block

try:
    with open("test.txt", "r") as reader:
        reader.read()
#except:
except Exception as e:
    print(f"test1 not found  {e}")
    print("test1 not found", str(e))
finally:
    print("Execution completed") # will always execute with or without exception
