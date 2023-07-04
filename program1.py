class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2


calculator = Calculator()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, or /): ")

if operator == '+':
    result = calculator.add(num1, num2)
elif operator == '-':
    result = calculator.subtract(num1, num2)
elif operator == '*':
    result = calculator.multiply(num1, num2)
elif operator == '/':
    try:
        result = calculator.divide(num1, num2)
    except ValueError as e:
        print("Error:", str(e))
        result = None
else:
    print("Invalid operator entered.")
    result = None

if result is not None:
    print("Result:", result)
