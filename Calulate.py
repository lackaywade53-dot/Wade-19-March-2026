#hi
# Team names:Group 5(Lee and Carter)
# Newman Dube, ....

# Description:
# This program demonstrates function definition, function calling,
# and a simple menu-driven addition operation.

# Function definition
def greet():
    # Function code
    print("Hello There")


# Function calling
greet()


# Function to add two numbers
def add(a, b):  # a and b are parameters
    c = a + b
    return c

def add(a, b):
 return a + b

def subtract(a, b):
 return a - b

def multiply(a, b):
 return a * b

def divide(a, b):
 if b == 0:
  return "Error: Division by zero!"
 return a / b

# Function call example
num1 = 3
num2 = 5

result = add(num1, num2)  # 3 and 5 are arguments
print("The sum is:", result)



# Menu-driven program
print("\nMenu:")
print("Press 1 to Add")
print("Press 2 to Subtract")
print("Press 3 to Multply")
print("Press 4 to Divide")



choice = int(input("What do you want to do? "))

# Taking user input (convert to integers)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if choice == 1:
    print("Result:", add(num1, num2))
else:
    print("Invalid choice")