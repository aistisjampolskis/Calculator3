result = 0

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def n_root(x, y):
    if x < 0 and y % 2 == 0:
        raise ValueError("Can't find even root of negative number")
    return x ** (1/y)

def reset():
    global memory
    memory = 0
    print("Memory reset.")