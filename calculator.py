#BASIC CALCULATOR PROGRAM

#CALCULATION FUNCTIONS
def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

#TO MAKE THE PROGRAM A BIT PRESENTABLE WHEN IT RUNS
print("###############################################################")
print("                     BASIC CALCULATOR")
print("###############################################################\n")
print("N.B. Only Addition, Subtraction, Multiplication and Division can be performed\n")
print("Enter 2 digits and the operation you want to perform with them\n")

#INPUT
digit1 = float(input("First Digit: "))
digit2 = float(input("Second Digit: "))
operation = input("The Operation: ")

#OPTIONS ON WHICH OPERATION IS GOING TO BER USED FOR CALCULATION
if operation == "+":
    result = add(digit1, digit2)
    print(result)
elif operation == "-":
    result = minus(digit1, digit2)
    print(result)
elif operation == "*" or operation == "x" or operation == "X":
    result = multiply(digit1, digit2)
    print(result)
elif operation == "/":
    result = divide(digit1, digit2)
    print(result)
else:
    print("Invalid Operation Entered!")
