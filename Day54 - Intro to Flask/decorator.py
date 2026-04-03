def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):    
    return n1 * n2

def divide(n1, n2):   
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def calculator(n1, n2, operation):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    func = operations.get(operation)
    if func:
        return func(n1, n2)
    else:
        return "Error: Invalid operation. Please choose from add, subtract, multiply, or divide."      
    
result = calculator(10, 5, "add")
print(result)

# nested function

# def outer_function():  
#     print("This is the outer function.")
    
#     def inner_function():
#         print("This is the inner function.")
    
#     inner_function()

# outer_function()

# function can be return from other function
def outer_function():  
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    return inner_function

inner_function = outer_function()

inner_function()

# python decorator
import random
import time

def decorator(func):
    def wrapper():
        # print("Before the function is called.")
        time.sleep(1)
        func()
        print("After the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

@decorator
def say_goodbye():
    print("Goodbye!")   

say_hello()
say_goodbye()

decorator(say_hello)()