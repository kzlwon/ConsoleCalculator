def subtract():
    return num1 - num2

def multiply():
    return num1 * num2

def devide():
    return num1 / num2

def add():
    return num1 + num2

bye = input('Press Enter to start:')

while bye != 'yes':
    stop = input('Want to quite?')
    if stop == 'quite':
        bye = False
        break
    else:
        num1 = int(input('Choose a number: '))
        num2 = int(input('Choose another number: '))
        choice = input('Type: subtract, multiply, devide or add: ')
        if choice == 'subtract':
            print(subtract())
        elif choice == 'multiply':
            print(multiply())
        elif choice == 'devide':
            print(devide())
        else:
            print(add())
