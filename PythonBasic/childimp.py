from OopsDemo import calculator


class inharitanceExp(calculator):
    num2= 200

    def __init__(self):
        calculator.__init__(self,2,2)
    def getCompleteData(self):
        return self.num2  + self.num +self.total()  #use self to access to parent class variable as well

inharitanceObj = inharitanceExp()
print(inharitanceObj.getCompleteData())

