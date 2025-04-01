# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
