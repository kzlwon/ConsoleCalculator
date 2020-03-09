def subtract():
    return num1 - num2

def multiply():
    return num1 * num2

def devide():
    return num1 / num2

def add():
    return num1 + num2


stop = "quit"

stop += input("Type quit to exit:")

for x in stop:
    if x == stop:
        break
    else:
        num1 = int(input('Choose a number: '))
        num2 = int(input('Choose another number: '))
        choice = str(input('Type: subtract, multiply, devide or add: '))
        if choice == 'subtract' or "-":
            print(subtract())
        elif choice == 'multiply' or "*":
            print(multiply())
        elif choice == 'devide' or "/":
            print(devide())
        elif choice == "add" or "+":
            print(add())