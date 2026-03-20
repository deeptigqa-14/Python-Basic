class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        if self.num1 >0 and self.num2>0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed"

a= int(input("Enter first number : "))
b= int(input("Enter second number : "))

calc = BasicCalculator(a, b)
print(f"Addition is {calc.num1} + {calc.num2} = {calc.addition()}")
print(f"Subtraction is {calc.num1} - {calc.num2} = {calc.subtraction()}")
print(f"Multiplication is {calc.num1} * {calc.num2} = {calc.multiplication()}")
print(f"Division is {calc.num1} / {calc.num2} = {calc.division()}")