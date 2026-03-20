from OopsDemo import calculator


class inharitanceExp(calculator):
    num2= 200

    def __init__(self,a,b):
        calculator.__init__(self,a,b)
    def getCompleteData(self):
        return self.num2  + self.num +self.total()  #use self to access to parent class variable as well

inharitanceObj = inharitanceExp(2,3)
print(inharitanceObj.getCompleteData())

