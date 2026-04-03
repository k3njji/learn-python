print("welcome to the calculator app")

def operation():
    print("+")
    print("-")
    print("*")
    print("/")

def calculate(first, second, op):
    if(op == '*'):
        return first*second
    
    if(op == '/'):
        return first/second
    
    if(op == '+'):
        return first+second
    
    if(op == '-'):
        return first-second

firstNumber = None
secondNumber = None

while True:
    if(firstNumber == None):
        firstNumber = float(input("input the first number: "))
    operation()
    op = input("pick an operation: ")
    secondNumber = float(input("pick the next number: "))
    total = calculate(firstNumber, secondNumber, op)

    print(f"{firstNumber} {op} {secondNumber} = {total}")
    
    cont = input(f"type 'y' to calculate using {total}, or 'n' to start a new one: ")

    if cont == 'y':
        firstNumber = total
    else:
        firstNumber = None