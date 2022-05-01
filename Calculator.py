def subtract(num1, num2):
        return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def devide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

while True:
    num1 = int(input('Choose a number: '))
    choice = input('Type >> +, -, *, /: ')
    num2 = int(input('Choose another number: '))
    if choice == '-':
        print(subtract(num1, num2))
    elif choice == '*':
        print(multiply(num1, num2))
    elif choice == '/':
        print(devide(num1, num2))
    elif choice == '+':
        print(add(num1, num2))
    stop = input("Type quit to exit: ")
    if stop == 'quit':
        break
    else:
        continue
