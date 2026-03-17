# self keword is mendatory in instance method
# constructor is a special method which is called when object is created
# it is used to initialize the instance variable
# if there is no constructor defined, default constructor is called
# class variable is shared by all objects of the class
# instance variable is unique to each object
# class variable is defined inside the class but outside any method
# instance variable is defined inside the constructor using self keyword

class calculator:
    #class variable are constant for all objects
    num = 100

    # default contractor called if there is no constructor defined
    def __init__(self, a, b): #called when object is created
        self.a = a # instance variable
        self.b = b
        print("I am in constructor")

    def getData(self):
        print("My 1st class in python")
    def total(self):
        return self.a + self.b + calculator.num # accessing class variable using class name or write self.num



calobj = calculator(20, 30) # creating object of class
calobj.getData()
print(calobj.total())

calobj1 = calculator(5, 8) # creating object of class
calobj1.getData()
print(calobj1.total())


