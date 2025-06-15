def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiple(a, b):
    return a * b

def div(a, b):
    return "Undefined" if b == 0 else a / b
print("Select operation: +, -, *, /")
op = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", sub(a, b))
elif op == '*':
    print("Result:", multiple(a, b))
elif op == '/':
    print("Result:", div(a, b))
else:
    print("Invalid operation")